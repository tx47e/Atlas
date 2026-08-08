const STORAGE_KEY = "atlasDashboardV3";
const SETTINGS_KEY = "atlasDashboardV3Settings";
if ("scrollRestoration" in history) history.scrollRestoration = "manual";

const deliverableLabels = {
  calcule: "Calcule",
  svg: "SVG-uri",
  markdown: "Markdown",
  html: "HTML",
};

const statusLabels = {
  noua: "Nouă",
  "date-validate": "Date validate",
  pregatita: "Pregătită",
  "in-lucru": "În lucru",
  "in-revizie": "În revizie",
  blocata: "Blocată",
  finalizata: "Finalizată",
  arhivata: "Arhivată",
};

const viewTitles = {
  dashboard: "Dashboard",
  calculator: "Calculator",
  vault: "Vault / Bibliotecă",
  agents: "Agenți",
  works: "Lucrări",
  persons: "Persoane",
  chronicles: "Noutăți / Cronici",
  archives: "Arhive",
  settings: "Setări",
};

const vaultDocuments = [
  { title: "Vibrații Fundamentale", category: "Numerologie", updated: "acum 2 ore" },
  { title: "Matricea Numelui", category: "Numerologie", updated: "acum 5 ore" },
  { title: "Arcana 22 — Interpretări", category: "Tarot", updated: "ieri" },
  { title: "Liniile Destinului în Matrice", category: "Matricea Destinului", updated: "acum 2 zile" },
  { title: "Formula Ciclurilor Personale", category: "Metode", updated: "acum 3 zile" },
];

const agents = [
  { name: "The Scribe", role: "Autor de lucrări", state: "working", task: "Redactează structura unei analize demonstrative", icon: "quill" },
  { name: "The Cartographer", role: "Creator de hărți SVG", state: "idle", task: "Disponibil pentru următorul grafic numerologic", icon: "compass" },
  { name: "The Lore Keeper", role: "Custodele Vaultului", state: "working", task: "Verifică legăturile și documentația din Vault", icon: "book" },
  { name: "Agent Dash", role: "Coordonator dashboard", state: "working", task: "Monitorizează manifestele și stările lucrărilor", icon: "shield" },
];

const chronicles = [
  { title: "Contractul Dashboard v3 a fost inițializat", text: "Interfața poate exporta manifestul, fără operații directe pe disc.", time: "astăzi", icon: "shield" },
  { title: "Biblioteca a fost indexată", text: "Documentele demonstrative sunt disponibile în secțiunea Vault.", time: "ieri", icon: "book" },
  { title: "Sistemul de iconuri a fost unificat", text: "Iconurile și ornamentele folosesc simboluri SVG scalabile.", time: "acum 2 zile", icon: "sun" },
];

const DEFAULT_PERSON_ID = "1984-11-06-SZABO-MIHAI-GABRIEL";
const seed = { persons: [], works: [] };

let state = loadState();
saveState();
let currentView = location.hash.replace("#/", "") || "dashboard";
if (!viewTitles[currentView]) currentView = "dashboard";
let activeWorkFilter = "toate";
let selectedCalculatorPersonKey = "";
let registryStatus = "loading";

const byId = id => document.getElementById(id);
const icon = name => `<svg aria-hidden="true"><use href="#${name}"></use></svg>`;
const escapeHtml = value => String(value ?? "").replace(/[&<>"']/g, character => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
}[character]));

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function loadState() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY));
    if (Array.isArray(stored?.works)) {
      return { persons: [], works: stored.works.filter(work => !String(work.id || "").startsWith("work-demo-")) };
    }
  } catch {}
  return clone(seed);
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify({ works: state.works }));
}

async function loadPersonsFromRegistry() {
  registryStatus = "loading";
  try {
    const response = await fetch("/api/persons", { cache: "no-store" });
    if (!response.ok) throw new Error(`Serviciul local a răspuns cu ${response.status}.`);
    const payload = await response.json();
    state.persons = (payload.persons || []).filter(person => person.fullName && person.birthDate && person.recordKey);
    registryStatus = payload.errors?.length ? "warning" : "ready";
  } catch (error) {
    state.persons = await loadLegacyPersonsFile();
    registryStatus = state.persons.length ? "legacy" : "error";
  }
  const selectedExists = state.persons.some(person => person.recordKey === selectedCalculatorPersonKey);
  if (!selectedExists) {
    selectedCalculatorPersonKey = state.persons.find(person => person.id === DEFAULT_PERSON_ID)?.recordKey
      || state.persons[0]?.recordKey
      || "";
  }
  renderView();
}

async function loadLegacyPersonsFile() {
  try {
    const response = await fetch("persoane.txt", { cache: "no-store" });
    if (!response.ok) return [];
    const text = await response.text();
    return text.split(/\r?\n/).map(line => line.trim()).filter(line => line && !line.startsWith("#")).map((line, index) => {
      const [label, fullName, activeName, familyName, birthDate, gender, referenceYear, yearLimit, partnerName, partnerBirthDate, partnerRelationship] = line.split("|");
      const id = `${birthDate}-${fullName.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase().replace(/[^A-Z0-9]+/g, "-")}`;
      return {
        schemaVersion: 1,
        id,
        recordKey: `legacy-${index}-${id}`,
        label,
        fullName,
        familyName,
        givenNames: fullName.replace(new RegExp(`^${familyName}\\s+`, "i"), ""),
        activeName,
        birthDate,
        birthTime: null,
        gender,
        previousNames: [],
        questions: [],
        relations: partnerName ? [{ fullName: partnerName, birthDate: partnerBirthDate || "", gender: "", type: partnerRelationship || "partener", status: "provizorie" }] : [],
        preferences: { template: "examen", expression: "conversational", detailLevel: "amplu", ageRange: { type: "complet", start: 0, end: Number(yearLimit) || 108 } },
        referenceYear: Number(referenceYear) || new Date().getFullYear(),
      };
    });
  } catch {
    return [];
  }
}

function personFor(work) {
  return state.persons.find(person => person.id === work.personId);
}

function progress(work) {
  if (!work.deliverables.length) return 0;
  return Math.round(work.deliverables.filter(item => item.state === "done").length / work.deliverables.length * 100);
}

function relativeDate(iso) {
  const difference = Math.max(0, Date.now() - new Date(iso).getTime());
  const hours = Math.floor(difference / 3600000);
  if (hours < 1) return "acum câteva minute";
  if (hours < 24) return `acum ${hours} ${hours === 1 ? "oră" : "ore"}`;
  const days = Math.floor(hours / 24);
  return `acum ${days} ${days === 1 ? "zi" : "zile"}`;
}

function navigate(view) {
  if (!viewTitles[view]) return;
  window.scrollTo({ top: 0, behavior: "auto" });
  currentView = view;
  location.hash = `/${view}`;
  document.querySelectorAll(".nav-item").forEach(button => button.classList.toggle("active", button.dataset.view === view));
  byId("pageTitle").textContent = viewTitles[view];
  byId("main").dataset.view = view;
  document.title = `${viewTitles[view]} — Atlas Numerologie`;
  renderView();
  closeSidebar();
  window.scrollTo({ top: 0, behavior: "auto" });
}

function renderView() {
  const renderers = {
    dashboard: renderDashboard,
    calculator: renderCalculator,
    vault: renderVault,
    agents: renderAgents,
    works: renderWorks,
    persons: renderPersons,
    chronicles: renderChronicles,
    archives: renderArchives,
    settings: renderSettings,
  };
  byId("view").innerHTML = renderers[currentView]();
  decorateCards();
  bindViewInteractions();
}

function decorateCards() {
  document.querySelectorAll(".card").forEach(card => {
    ["tl", "tr", "br", "bl"].forEach(position => {
      const corner = document.createElement("span");
      corner.className = `card-corner corner-${position}`;
      corner.setAttribute("aria-hidden", "true");
      corner.innerHTML = '<img src="assets/lace-corner.svg" alt="">';
      card.append(corner);
    });
  });
}

function renderCalculator() {
  return `
    <section class="calculator-surface" aria-label="Calculator numerologic">
      <div class="calculator-person-tools" aria-label="Selectare persoană pentru calculator">
        <select id="calculatorHostPersonSelect" aria-label="Persoană salvată">
          ${state.persons.length
            ? state.persons.map(person => `<option value="${escapeHtml(person.recordKey)}" ${person.recordKey === selectedCalculatorPersonKey ? "selected" : ""}>${escapeHtml(personOptionLabel(person))}</option>`).join("")
            : `<option value="">${registryStatus === "loading" ? "Se scanează registrul persoane…" : "Nu există persoane în registru"}</option>`}
        </select>
        <button id="calculatorHostLoadBtn" class="secondary-button" type="button">Încarcă</button>
        <button id="calculatorHostNewBtn" class="secondary-button" type="button">Persoană nouă</button>
      </div>
      <iframe
        class="calculator-frame"
        src="calculator.html?v=20260808-2"
        title="Calculator numerologic Atlas"
        loading="eager"
        scrolling="yes"
      ></iframe>
    </section>
  `;
}

function formatDateRo(isoDate) {
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(isoDate || "");
  return match ? `${match[3]}.${match[2]}.${match[1]}` : "Data necunoscută";
}

function personOptionLabel(person) {
  return `${person.fullName} — ${formatDateRo(person.birthDate)}`;
}

function renderDashboard() {
  const active = state.works.filter(work => ["pregatita", "in-lucru", "in-revizie"].includes(work.status)).length;
  const finished = state.works.filter(work => work.status === "finalizata").length;
  const recentWorks = [...state.works].sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt)).slice(0, 5);
  return `
    <div class="metric-grid">
      ${metricCard("book", "Documente în Vault", vaultDocuments.length)}
      ${metricCard("quill", "Lucrări active", active)}
      ${metricCard("compass", "Persoane înregistrate", state.persons.length)}
      ${metricCard("shield", "Agenți disponibili", agents.length)}
    </div>
    <div class="dashboard-columns">
      <article class="card panel-card">
        <div class="card-heading"><h2>Lucrări recente</h2>${icon("quill")}</div>
        <div class="rows">
          ${recentWorks.map(work => `<div class="data-row"><span class="row-title">${escapeHtml(work.title)}</span><span class="status ${work.status}">${statusLabels[work.status]}</span></div>`).join("")}
        </div>
        <button class="card-link" data-go="works">Vezi toate lucrările ${icon("arrow")}</button>
      </article>
      <article class="card panel-card">
        <div class="card-heading"><h2>Actualizări în Vault</h2>${icon("book")}</div>
        <div class="rows">
          ${vaultDocuments.slice(0, 5).map(document => `<div class="data-row"><span class="row-title">${escapeHtml(document.title)}</span><span class="row-meta">${document.updated}</span></div>`).join("")}
        </div>
        <button class="card-link" data-go="vault">Deschide biblioteca ${icon("arrow")}</button>
      </article>
      <article class="card panel-card">
        <div class="card-heading"><h2>Activitatea agenților</h2>${icon("sun")}</div>
        ${agents.map(agent => `<div class="activity-row"><span class="activity-icon">${icon(agent.icon)}</span><div><strong>${agent.name}</strong><p>${agent.state === "working" ? "Lucrează acum" : "Disponibil"}</p></div><time>${agent.state === "working" ? "acum" : "18 min"}</time></div>`).join("")}
        <button class="card-link" data-go="agents">Vezi activitatea ${icon("arrow")}</button>
      </article>
    </div>
    <div class="dashboard-note" hidden>${finished} lucrări finalizate</div>`;
}

function metricCard(iconName, label, value) {
  return `<article class="card metric-card"><span class="metric-icon">${icon(iconName)}</span><div><p>${label}</p><strong>${value}</strong></div></article>`;
}

function renderVault() {
  return `
    <div class="section-toolbar">
      <h2>Colecțiile Atlas</h2>
      <label class="search-control">${icon("search")}<input id="vaultSearch" placeholder="Caută în bibliotecă"></label>
    </div>
    <div class="feature-grid">
      <article class="card feature-card" data-category="Numerologie"><img class="vault-art" src="assets/vault-card-numerologie-hd.svg" alt="Pătratul lui Pitagora cu cifrele 1–2–3, 4–5–6 și 7–8–9 dispuse pe coloane"><h3>Numerologie</h3><p>Metode, formule și interpretări</p></article>
      <article class="card feature-card" data-category="Tarot"><img class="vault-art tarot-art" src="assets/vault-card-tarot-detailed-transparent.png?v=20260802-7" alt="Trei cărți de Tarot gravate în detaliu, pe fundal transparent: The Moon XVIII, Arcana 0 — The Fool și The Star XVII"><h3>Tarot</h3><p>Arcane și corespondențe</p></article>
      <article class="card feature-card" data-category="Matricea Destinului"><img class="vault-art" src="assets/vault-card-matricea-destinului-hd.svg" alt="Matricea Destinului, diagramă circulară vectorială inspirată din Floarea Vieții"><h3>Matricea Destinului</h3><p>Linii, energii și profiluri</p></article>
    </div>
    <article class="card panel-card" style="margin-top:15px">
      <div class="card-heading"><h2>Documente recente</h2>${icon("book")}</div>
      <div id="vaultRows">${vaultRows(vaultDocuments)}</div>
    </article>`;
}

function vaultRows(documents) {
  return documents.map(document => `<div class="data-row"><span><strong class="row-title">${escapeHtml(document.title)}</strong><small class="row-meta">${escapeHtml(document.category)}</small></span><span class="row-meta">${document.updated}</span></div>`).join("") || `<div class="empty-state"><p>Niciun document pentru această căutare.</p></div>`;
}

function renderAgents() {
  return `
    <div class="section-toolbar"><h2>Echipa Atlas</h2><button class="secondary-button" id="refreshAgents">${icon("clock")}Actualizează starea</button></div>
    <div class="agent-grid">
      ${agents.map(agent => `<article class="card agent-card"><div class="agent-seal">${icon(agent.icon)}</div><div><h3>${agent.name}</h3><p>${agent.role}</p><p style="margin-top:8px">${agent.task}</p><span class="agent-state ${agent.state === "idle" ? "idle" : ""}">${agent.state === "working" ? "Lucrează" : "Disponibil"}</span></div></article>`).join("")}
    </div>`;
}

function renderWorks() {
  const filtered = activeWorkFilter === "toate" ? state.works : state.works.filter(work => work.status === activeWorkFilter);
  const tabs = ["toate", "pregatita", "in-lucru", "in-revizie", "finalizata"];
  return `
    <div class="section-toolbar"><h2>Registrul lucrărilor</h2><button class="primary-button" data-new-work>${icon("plus")}Lucrare nouă</button></div>
    <article class="card table-card">
      <div class="table-tabs">${tabs.map(tab => `<button class="table-tab ${activeWorkFilter === tab ? "active" : ""}" data-work-filter="${tab}">${tab === "toate" ? "Toate" : statusLabels[tab]}</button>`).join("")}</div>
      <div id="workRows">
        ${filtered.map(work => {
          const person = personFor(work);
          return `<div class="work-row"><span><strong>${escapeHtml(work.title)}</strong><small class="row-meta">${escapeHtml(person?.fullName || "Persoană lipsă")}</small></span><span class="status ${work.status}">${statusLabels[work.status]}</span><span>${progress(work)}% complet</span><button aria-label="Exportă manifestul" data-export="${work.id}">${icon("download")}</button></div>`;
        }).join("") || `<div class="empty-state"><p>Nu există lucrări în această categorie.</p></div>`}
      </div>
    </article>`;
}

function renderPersons() {
  return `
    <div class="section-toolbar"><h2>Persoane înregistrate</h2><label class="search-control">${icon("search")}<input id="personSearch" placeholder="Caută o persoană"></label></div>
    <div class="person-grid" id="personGrid">${personCards(state.persons)}</div>`;
}

function personCards(persons) {
  return persons.map(person => {
    const count = state.works.filter(work => work.personId === person.id).length;
    return `<article class="card person-card"><div class="person-head"><div class="avatar">${icon("person")}</div><div><h3>${escapeHtml(person.fullName)}</h3><p>${new Date(`${person.birthDate}T12:00:00`).toLocaleDateString("ro-RO")}</p></div></div><p style="margin-top:13px">${count} ${count === 1 ? "lucrare asociată" : "lucrări asociate"}</p></article>`;
  }).join("") || `<div class="empty-state"><p>Nicio persoană pentru această căutare.</p></div>`;
}

function renderChronicles() {
  return `<div class="section-toolbar"><h2>Jurnalul Atlas</h2></div><div class="chronicle-list">${chronicles.map(item => `<article class="card chronicle-card">${icon(item.icon)}<div><h3>${item.title}</h3><p>${item.text}</p></div><time>${item.time}</time></article>`).join("")}</div>`;
}

function renderArchives() {
  const archived = state.works.filter(work => work.status === "arhivata");
  if (!archived.length) return `<div class="empty-state">${icon("archive")}<div><h2>Arhiva este pregătită</h2><p>Lucrările arhivate vor apărea aici, păstrate separat de registrul activ.</p></div></div>`;
  return `<article class="card panel-card">${archived.map(work => `<div class="data-row"><span>${escapeHtml(work.title)}</span><span>${relativeDate(work.updatedAt)}</span></div>`).join("")}</article>`;
}

function renderSettings() {
  const settings = loadSettings();
  return `
    <div class="settings-layout">
      <aside class="card settings-menu">
        <button class="active">Preferințe</button><button>Notificări</button><button>Export</button><button>Cont</button>
      </aside>
      <section class="card settings-panel">
        <h2>Preferințe</h2>
        <div class="setting-row"><label for="languageSetting">Limbă</label><select id="languageSetting"><option>Română</option></select></div>
        <div class="setting-row"><label for="densitySetting">Densitate dashboard</label><select id="densitySetting"><option ${settings.density === "Confortabil" ? "selected" : ""}>Confortabil</option><option ${settings.density === "Compact" ? "selected" : ""}>Compact</option></select></div>
        <div class="setting-row"><label>Afișează activitatea agenților</label><button class="switch ${settings.showAgents ? "" : "off"}" data-setting="showAgents" aria-label="Comută activitatea agenților"></button></div>
        <div class="setting-row"><label>Activează notificările locale</label><button class="switch ${settings.notifications ? "" : "off"}" data-setting="notifications" aria-label="Comută notificările"></button></div>
        <div style="margin-top:20px"><button class="primary-button" id="saveSettings">Salvează modificările</button></div>
      </section>
    </div>`;
}

function loadSettings() {
  try {
    return { density: "Confortabil", showAgents: true, notifications: true, ...JSON.parse(localStorage.getItem(SETTINGS_KEY)) };
  } catch {
    return { density: "Confortabil", showAgents: true, notifications: true };
  }
}

function bindViewInteractions() {
  document.querySelectorAll("[data-go]").forEach(button => button.addEventListener("click", () => navigate(button.dataset.go)));
  document.querySelectorAll("[data-new-work]").forEach(button => button.addEventListener("click", openWorkDialog));
  document.querySelectorAll("[data-work-filter]").forEach(button => button.addEventListener("click", () => {
    activeWorkFilter = button.dataset.workFilter;
    renderView();
  }));
  document.querySelectorAll("[data-export]").forEach(button => button.addEventListener("click", () => exportManifest(button.dataset.export)));
  document.querySelectorAll("[data-category]").forEach(card => card.addEventListener("click", () => {
    const documents = vaultDocuments.filter(item => item.category === card.dataset.category);
    byId("vaultRows").innerHTML = vaultRows(documents);
    toast(`Colecția ${card.dataset.category} este deschisă`);
  }));
  byId("vaultSearch")?.addEventListener("input", event => {
    const query = event.target.value.toLocaleLowerCase("ro");
    byId("vaultRows").innerHTML = vaultRows(vaultDocuments.filter(item => `${item.title} ${item.category}`.toLocaleLowerCase("ro").includes(query)));
  });
  byId("personSearch")?.addEventListener("input", event => {
    const query = event.target.value.toLocaleLowerCase("ro");
    byId("personGrid").innerHTML = personCards(state.persons.filter(person => person.fullName.toLocaleLowerCase("ro").includes(query)));
  });
  byId("refreshAgents")?.addEventListener("click", () => toast("Starea agenților a fost actualizată"));
  document.querySelectorAll("[data-setting]").forEach(button => button.addEventListener("click", () => button.classList.toggle("off")));
  byId("saveSettings")?.addEventListener("click", () => {
    const switches = document.querySelectorAll("[data-setting]");
    const settings = {
      density: byId("densitySetting").value,
      showAgents: !switches[0].classList.contains("off"),
      notifications: !switches[1].classList.contains("off"),
    };
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
    document.documentElement.dataset.density = settings.density === "Compact" ? "compact" : "comfortable";
    toast("Preferințele au fost salvate");
  });
  if (currentView === "calculator") bindCalculatorPersonTools();
}

function bindCalculatorPersonTools() {
  const frame = document.querySelector(".calculator-frame");
  const hostSelect = byId("calculatorHostPersonSelect");
  const hostLoad = byId("calculatorHostLoadBtn");
  const hostNew = byId("calculatorHostNewBtn");
  if (!frame || !hostSelect || !hostLoad || !hostNew) return;

  const selectedPerson = () => state.persons.find(person => person.recordKey === hostSelect.value);
  const applySelectedPerson = () => {
    const innerDocument = frame.contentDocument;
    const innerWindow = frame.contentWindow;
    const person = selectedPerson();
    if (!innerDocument || !innerWindow || !person) return false;
    const relation = person.relations?.[0];
    const values = {
      fullName: person.fullName,
      activeName: person.activeName || person.givenNames?.split(/\s+/)[0] || "",
      familyName: person.familyName || "",
      birthDate: person.birthDate,
      gender: person.gender || "masculin",
      referenceYear: person.referenceYear || new Date().getFullYear(),
      yearLimit: person.preferences?.ageRange?.end || 108,
      partnerName: relation?.fullName || "",
      partnerBirthDate: relation?.birthDate || "",
      partnerRelationship: relation ? (/sot|sotie/i.test(relation.type) ? "sot/sotie" : /iubit|iubita/i.test(relation.type) ? "iubit/a" : "partener") : "partener",
      workNotes: (person.questions || []).map(question => `[${question.category}] ${question.text}`).join("\n"),
    };
    Object.entries(values).forEach(([id, value]) => {
      const control = innerDocument.getElementById(id);
      if (!control) return;
      control.value = value;
      control.dispatchEvent(new Event("change", { bubbles: true }));
    });
    innerWindow.setPartnerFieldsActive?.(Boolean(relation));
    innerWindow.renderTable?.();
    selectedCalculatorPersonKey = person.recordKey;
    toast(`${person.fullName} a fost încărcat în calculator`);
    return true;
  };

  const connect = () => applySelectedPerson();
  hostSelect.addEventListener("change", () => {
    selectedCalculatorPersonKey = hostSelect.value;
    applySelectedPerson();
  });
  hostLoad.addEventListener("click", openImportPersonDialog);
  hostNew.addEventListener("click", openPersonDialog);
  frame.addEventListener("load", connect, { once: true });
  if (frame.contentDocument?.readyState === "complete") connect();
}

function openPersonDialog() {
  const form = byId("personForm");
  form.reset();
  byId("personFormError").textContent = "";
  byId("hasRelations").checked = false;
  byId("relationsEditor").hidden = true;
  byId("ageRangeType").value = "complet";
  byId("ageRangeStart").value = "0";
  byId("ageRangeEnd").value = "108";
  byId("ageRangeStart").disabled = true;
  byId("ageRangeEnd").disabled = true;
  byId("hasBirthTime").checked = false;
  byId("birthTimeField").hidden = true;
  byId("birthTimeInput").disabled = true;
  byId("birthTimeInput").value = "";
  byId("relationRows").innerHTML = "";
  byId("questionRows").innerHTML = questionRowTemplate();
  byId("personDialog").showModal();
  setTimeout(() => form.elements.fullName.focus(), 50);
}

function openImportPersonDialog() {
  const form = byId("importPersonForm");
  form.reset();
  byId("importPersonFileName").textContent = "Alege un fișier .yaml sau .yml.";
  byId("importPersonError").textContent = "";
  byId("importPersonDialog").showModal();
}

function relationRowTemplate() {
  return `<fieldset class="repeat-row relation-row">
    <legend>Persoană asociată</legend>
    <button class="remove-repeat" type="button" data-remove-row aria-label="Elimină persoana">×</button>
    <div class="form-grid relation-grid">
      <label class="span-2">Nume complet<input data-relation-field="fullName" autocomplete="off" required></label>
      <fieldset class="relation-date-field span-2">
        <legend>Data nașterii</legend>
        <div class="relation-date-parts">
          <label>Zi<input data-relation-field="birthDay" type="number" min="1" max="31" inputmode="numeric" placeholder="ZZ" required></label>
          <label>Lună<input data-relation-field="birthMonth" type="number" min="1" max="12" inputmode="numeric" placeholder="LL" required></label>
          <label>An<input data-relation-field="birthYear" type="number" min="1900" max="2100" inputmode="numeric" placeholder="AAAA" required></label>
          <label class="relation-calendar-picker"><span>Calendar</span><input data-relation-calendar type="date" aria-label="Alege data nașterii din calendar"></label>
        </div>
      </fieldset>
      <label>Gen<select data-relation-field="gender" required><option value="">Alege</option><option value="masculin">Masculin</option><option value="feminin">Feminin</option></select></label>
      <label>Tipul relației<select data-relation-field="type" required><option value="partener">Partener</option><option value="sot">Soț</option><option value="sotie">Soție</option><option value="iubit">Iubit</option><option value="iubita">Iubită</option><option value="familie">Familie</option><option value="altul">Altul</option></select></label>
    </div>
  </fieldset>`;
}

function questionRowTemplate() {
  return `<div class="repeat-row question-row">
    <label>Categorie<select data-question-field="category"><option value="cariera">Carieră</option><option value="iubire">Iubire</option><option value="relatie">Relație</option><option value="familie">Familie</option><option value="finante">Finanțe</option><option value="sanatate">Sănătate</option><option value="alta">Altă întrebare</option></select></label>
    <label class="question-text">Întrebare<textarea data-question-field="text" rows="2" placeholder="Scrie întrebarea persoanei"></textarea></label>
    <button class="remove-repeat" type="button" data-remove-row aria-label="Elimină întrebarea">×</button>
  </div>`;
}

function isoDateFromParts(dayValue, monthValue, yearValue) {
  const day = Number(dayValue);
  const month = Number(monthValue);
  const year = Number(yearValue);
  if (!Number.isInteger(day) || !Number.isInteger(month) || !Number.isInteger(year)) return null;
  const date = new Date(Date.UTC(year, month - 1, day));
  if (date.getUTCFullYear() !== year || date.getUTCMonth() !== month - 1 || date.getUTCDate() !== day) return null;
  if (date > new Date()) return null;
  return `${String(year).padStart(4, "0")}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
}

function personIdFor(fullName, birthDate) {
  const safeName = fullName.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .toUpperCase().replace(/[^A-Z0-9]+/g, "-").replace(/^-|-$/g, "");
  return `${birthDate}-${safeName}`;
}

function collectPersonForm() {
  const form = byId("personForm");
  const data = new FormData(form);
  const fullName = `${data.get("fullName") || ""}`.trim();
  const familyName = `${data.get("familyName") || ""}`.trim();
  const givenNames = `${data.get("givenNames") || ""}`.trim();
  const activeName = `${data.get("activeName") || ""}`.trim();
  const gender = `${data.get("gender") || ""}`;
  const birthTime = byId("hasBirthTime").checked ? (`${data.get("birthTime") || ""}` || null) : null;
  const previousNames = `${data.get("previousNames") || ""}`.split(",").map(value => value.trim()).filter(Boolean);
  const birthDate = isoDateFromParts(data.get("birthDay"), data.get("birthMonth"), data.get("birthYear"));
  if (!fullName || !familyName || !givenNames || !activeName || !gender || !birthDate) {
    throw new Error("Completează identitatea și introdu o dată de naștere validă, în format zi, lună, an.");
  }

  const relations = byId("hasRelations").checked ? [...byId("relationRows").querySelectorAll(".relation-row")].map(row => {
    const value = field => row.querySelector(`[data-relation-field="${field}"]`)?.value.trim() || "";
    const relation = {
      fullName: value("fullName"),
      birthDate: isoDateFromParts(value("birthDay"), value("birthMonth"), value("birthYear")),
      gender: value("gender"),
      type: value("type"),
    };
    if (!relation.fullName || !relation.birthDate || !relation.gender || !relation.type) {
      throw new Error("Completează toate datele pentru fiecare persoană din secțiunea Relații.");
    }
    const registered = state.persons.find(person => person.fullName.toLocaleLowerCase("ro") === relation.fullName.toLocaleLowerCase("ro") && person.birthDate === relation.birthDate);
    return { ...relation, personId: registered?.id || null, status: registered ? "confirmata" : "provizorie" };
  }) : [];
  if (byId("hasRelations").checked && !relations.length) throw new Error("Adaugă cel puțin o persoană în secțiunea Relații.");

  const questions = [...byId("questionRows").querySelectorAll(".question-row")].map(row => ({
    category: row.querySelector('[data-question-field="category"]').value,
    text: row.querySelector('[data-question-field="text"]').value.trim(),
  })).filter(question => question.text);
  const id = personIdFor(fullName, birthDate);
  const now = new Date().toISOString();
  const ageRangeType = `${data.get("ageRangeType") || "complet"}`;
  const ageRange = ageRangeType === "specific"
    ? { type: "specific", start: Number(data.get("ageRangeStart")), end: Number(data.get("ageRangeEnd")) }
    : { type: "complet", start: 0, end: 108 };
  if (!Number.isInteger(ageRange.start) || !Number.isInteger(ageRange.end) || ageRange.start < 0 || ageRange.end > 108 || ageRange.start >= ageRange.end) {
    throw new Error("Intervalul de vârstă trebuie să fie între 0 și 108, în ordine crescătoare.");
  }
  return {
    schemaVersion: 1,
    id,
    fullName,
    familyName,
    givenNames,
    activeName,
    birthDate,
    birthTime,
    gender,
    previousNames,
    questions,
    relations,
    preferences: {
      template: `${data.get("template") || "examen"}`,
      expression: "conversational",
      detailLevel: "amplu",
      ageRange,
    },
    metadata: { createdAt: now, updatedAt: now },
  };
}

function personToApiDocument(person) {
  return {
    schema_version: 1,
    id: person.id,
    identitate: {
      nume_complet: person.fullName,
      nume_familie: person.familyName,
      prenume: person.givenNames,
      prenume_activ: person.activeName,
      data_nasterii: person.birthDate,
      ora_nasterii: person.birthTime,
      gen: person.gender,
      nume_anterioare: person.previousNames,
    },
    preferinte_lucrare: {
      template: person.preferences.template,
      exprimare: person.preferences.expression,
      nivel_detaliere: person.preferences.detailLevel,
      interval_ani: {
        tip: person.preferences.ageRange.type,
        start_varsta: person.preferences.ageRange.start,
        final_varsta: person.preferences.ageRange.end,
      },
    },
    intrebari: person.questions.map(question => ({ categorie: question.category, text: question.text })),
    relatii: person.relations.map(relation => ({
      persoana_id: relation.personId,
      nume: relation.fullName,
      data_nasterii: relation.birthDate,
      gen: relation.gender,
      tip: relation.type,
      status: relation.status,
    })),
  };
}

function yamlString(value) {
  return JSON.stringify(String(value ?? ""));
}

function yamlForPerson(person) {
  const questions = person.questions.length
    ? person.questions.map(question => `  - categorie: ${yamlString(question.category)}\n    text: ${yamlString(question.text)}`).join("\n")
    : "  []";
  const relations = person.relations.length
    ? person.relations.map(relation => `  - persoana_id: ${relation.personId ? yamlString(relation.personId) : "null"}\n    nume: ${yamlString(relation.fullName)}\n    data_nasterii: ${yamlString(relation.birthDate)}\n    gen: ${yamlString(relation.gender)}\n    tip: ${yamlString(relation.type)}\n    status: ${yamlString(relation.status)}`).join("\n")
    : "  []";
  return `schema_version: 1
id: ${yamlString(person.id)}
identitate:
  nume_complet: ${yamlString(person.fullName)}
  nume_familie: ${yamlString(person.familyName)}
  prenume: ${yamlString(person.givenNames)}
  prenume_activ: ${yamlString(person.activeName)}
  data_nasterii: ${yamlString(person.birthDate)}
  ora_nasterii: ${person.birthTime ? yamlString(person.birthTime) : "null"}
  gen: ${yamlString(person.gender)}
  nume_anterioare: ${person.previousNames?.length ? `[${person.previousNames.map(yamlString).join(", ")}]` : "[]"}
preferinte_lucrare:
  template: ${yamlString(person.preferences.template)}
  exprimare: ${yamlString(person.preferences.expression)}
  nivel_detaliere: ${yamlString(person.preferences.detailLevel)}
  interval_ani:
    tip: ${yamlString(person.preferences.ageRange.type)}
    start_varsta: ${person.preferences.ageRange.start}
    final_varsta: ${person.preferences.ageRange.end}
intrebari:
${questions}
relatii:
${relations}
metadata:
  created_at: ${yamlString(person.metadata.createdAt)}
  updated_at: ${yamlString(person.metadata.updatedAt)}
`;
}

function downloadPersonYaml(person) {
  const blob = new Blob([yamlForPerson(person)], { type: "application/yaml;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  const timestamp = new Date().toISOString().replace(/\.\d{3}Z$/, "Z").replace("T", "_").replace(/:/g, "-").replace("Z", "");
  link.download = `${person.id}__${timestamp}.yaml`;
  link.click();
  URL.revokeObjectURL(link.href);
}

function openWorkDialog() {
  byId("workForm").reset();
  byId("formError").textContent = "";
  byId("workDialog").showModal();
}

function manifestFor(work) {
  const person = personFor(work);
  return {
    schemaVersion: "1.0",
    taskId: `task-${work.id}`,
    createdAt: new Date().toISOString(),
    person,
    work: {
      id: work.id,
      title: work.title,
      workType: work.workType,
      targetDirectory: work.targetDirectory,
    },
    requestedSkills: ["numerologie-dashboard", "numerologie-lucrare-redactare"],
    requestedDeliverables: work.deliverables.map(({ type, label }) => ({ type, label })),
    initialStatus: work.status,
    blockers: [...work.blockers],
  };
}

function exportManifest(id) {
  const work = state.works.find(item => item.id === id);
  if (!work) return;
  const blob = new Blob([JSON.stringify(manifestFor(work), null, 2)], { type: "application/json" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = `${work.id}-manifest.json`;
  link.click();
  URL.revokeObjectURL(link.href);
  toast("Manifestul JSON a fost exportat");
}

function toast(message) {
  const element = byId("toast");
  element.textContent = message;
  element.classList.add("show");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => element.classList.remove("show"), 2400);
}

function closeSidebar() {
  byId("sidebar").classList.remove("open");
  byId("menuToggle").setAttribute("aria-expanded", "false");
}

document.querySelectorAll(".nav-item").forEach(button => button.addEventListener("click", () => navigate(button.dataset.view)));
byId("newWorkBtn")?.addEventListener("click", openWorkDialog);
byId("menuToggle").addEventListener("click", () => {
  const open = byId("sidebar").classList.toggle("open");
  byId("menuToggle").setAttribute("aria-expanded", String(open));
});
byId("logoutBtn").addEventListener("click", () => toast("Sesiunea demonstrativă rămâne locală în acest browser"));
byId("notificationBtn").addEventListener("click", () => toast("Ai 3 actualizări noi în Atlas"));
byId("searchBtn").addEventListener("click", () => {
  byId("searchDialog").showModal();
  setTimeout(() => byId("globalSearchInput").focus(), 50);
});

byId("globalSearchInput").addEventListener("input", event => {
  const query = event.target.value.toLocaleLowerCase("ro").trim();
  if (!query) {
    byId("globalSearchResults").innerHTML = `<p class="row-meta">Scrie cel puțin un cuvânt pentru a căuta.</p>`;
    return;
  }
  const results = [
    ...state.persons.map(item => ({ type: "Persoană", title: item.fullName, view: "persons" })),
    ...state.works.map(item => ({ type: "Lucrare", title: item.title, view: "works" })),
    ...vaultDocuments.map(item => ({ type: "Vault", title: item.title, view: "vault" })),
  ].filter(item => item.title.toLocaleLowerCase("ro").includes(query)).slice(0, 8);
  byId("globalSearchResults").innerHTML = results.map(item => `<button class="search-result" type="button" data-search-go="${item.view}"><span>${escapeHtml(item.title)}</span><small>${item.type}</small></button>`).join("") || `<p class="row-meta">Nu am găsit rezultate.</p>`;
  document.querySelectorAll("[data-search-go]").forEach(button => button.addEventListener("click", () => {
    byId("searchDialog").close();
    navigate(button.dataset.searchGo);
  }));
});

byId("hasRelations").addEventListener("change", event => {
  byId("relationsEditor").hidden = !event.target.checked;
  if (event.target.checked && !byId("relationRows").children.length) {
    byId("relationRows").insertAdjacentHTML("beforeend", relationRowTemplate());
  }
});
byId("addRelationBtn").addEventListener("click", () => {
  byId("relationRows").insertAdjacentHTML("beforeend", relationRowTemplate());
});
byId("relationRows").addEventListener("change", event => {
  const calendar = event.target.closest("[data-relation-calendar]");
  if (!calendar?.value) return;
  const [year, month, day] = calendar.value.split("-");
  const row = calendar.closest(".relation-row");
  row.querySelector('[data-relation-field="birthDay"]').value = Number(day);
  row.querySelector('[data-relation-field="birthMonth"]').value = Number(month);
  row.querySelector('[data-relation-field="birthYear"]').value = Number(year);
});
byId("relationRows").addEventListener("input", event => {
  if (!event.target.matches('[data-relation-field="birthDay"], [data-relation-field="birthMonth"], [data-relation-field="birthYear"]')) return;
  const row = event.target.closest(".relation-row");
  const value = field => row.querySelector(`[data-relation-field="${field}"]`).value;
  row.querySelector("[data-relation-calendar]").value = isoDateFromParts(value("birthDay"), value("birthMonth"), value("birthYear")) || "";
});
byId("addQuestionBtn").addEventListener("click", () => {
  byId("questionRows").insertAdjacentHTML("beforeend", questionRowTemplate());
});
byId("ageRangeType").addEventListener("change", event => {
  const specific = event.target.value === "specific";
  byId("ageRangeStart").disabled = !specific;
  byId("ageRangeEnd").disabled = !specific;
});
byId("hasBirthTime").addEventListener("change", event => {
  const enabled = event.target.checked;
  byId("birthTimeField").hidden = !enabled;
  byId("birthTimeInput").disabled = !enabled;
  if (!enabled) byId("birthTimeInput").value = "";
});
byId("personDialogCloseBtn").addEventListener("click", () => byId("personDialog").close());
byId("importPersonDialogCloseBtn").addEventListener("click", () => byId("importPersonDialog").close());
byId("importPersonDialogCancelBtn").addEventListener("click", () => byId("importPersonDialog").close());
byId("personYamlFile").addEventListener("change", event => {
  const file = event.target.files?.[0];
  byId("importPersonFileName").textContent = file ? `${file.name} · ${Math.max(1, Math.ceil(file.size / 1024))} KB` : "Alege un fișier .yaml sau .yml.";
  byId("importPersonError").textContent = "";
});
byId("importPersonForm").addEventListener("submit", async event => {
  event.preventDefault();
  const file = byId("personYamlFile").files?.[0];
  const error = byId("importPersonError");
  error.textContent = "";
  if (!file) {
    error.textContent = "Alege mai întâi un fișier YAML.";
    return;
  }
  if (!/\.ya?ml$/i.test(file.name)) {
    error.textContent = "Fișierul trebuie să aibă extensia .yaml sau .yml.";
    return;
  }
  try {
    const response = await fetch("/api/persons/import", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ filename: file.name, yaml: await file.text() }),
    });
    const result = await response.json().catch(() => ({}));
    if (!response.ok || !result.ok) throw new Error(result.error || "Fișierul YAML nu a putut fi importat.");
    selectedCalculatorPersonKey = result.person.recordKey;
    byId("importPersonDialog").close();
    await loadPersonsFromRegistry();
    toast(`${result.person.fullName} a fost adăugat în registru și încărcat în calculator`);
  } catch (exception) {
    error.textContent = exception.message || "Fișierul YAML nu a putut fi importat.";
  }
});
byId("personForm").addEventListener("click", event => {
  const removeButton = event.target.closest("[data-remove-row]");
  if (!removeButton) return;
  const row = removeButton.closest(".repeat-row");
  row?.remove();
  if (byId("hasRelations").checked && !byId("relationRows").children.length) {
    byId("hasRelations").checked = false;
    byId("relationsEditor").hidden = true;
  }
});
byId("personForm").addEventListener("submit", async event => {
  if (event.submitter?.value === "cancel") {
    event.preventDefault();
    byId("personDialog").close();
    return;
  }
  event.preventDefault();
  const error = byId("personFormError");
  error.textContent = "";
  if (!event.currentTarget.reportValidity()) return;
  try {
    const person = collectPersonForm();
    const response = await fetch("/api/persons", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(personToApiDocument(person)),
    });
    const result = await response.json().catch(() => ({}));
    if (!response.ok || !result.ok) throw new Error(result.error || "Serviciul local nu a putut salva fișa YAML.");
    selectedCalculatorPersonKey = result.person.recordKey;
    byId("personDialog").close();
    if (event.submitter?.hasAttribute("data-export-yaml")) downloadPersonYaml(result.person);
    await loadPersonsFromRegistry();
    toast(`${person.fullName} a fost salvat direct în Dashboard/v3/persoane`);
  } catch (exception) {
    error.textContent = exception.message || "Datele persoanei nu au putut fi salvate.";
  }
});

byId("workForm").addEventListener("submit", event => {
  if (event.submitter?.value === "cancel") return;
  event.preventDefault();
  const data = new FormData(event.currentTarget);
  const fullName = data.get("fullName")?.trim();
  const birthDate = data.get("birthDate");
  const workType = data.get("workType");
  const targetDirectory = data.get("targetDirectory")?.trim();
  const deliverables = data.getAll("deliverables");
  if (!fullName || !birthDate || !workType || !targetDirectory || !deliverables.length) {
    byId("formError").textContent = "Completează câmpurile obligatorii și alege cel puțin un livrabil.";
    return;
  }
  const identity = `${fullName.toLocaleLowerCase("ro")}|${birthDate}`;
  let person = state.persons.find(item => `${item.fullName.toLocaleLowerCase("ro")}|${item.birthDate}` === identity);
  if (!person) {
    byId("formError").textContent = "Persoana nu există în registrul YAML. Creeaz-o mai întâi din Calculator → Persoană nouă.";
    return;
  }
  const id = `work-${crypto.randomUUID()}`;
  const now = new Date().toISOString();
  const work = {
    id,
    personId: person.id,
    title: `${workType} — ${fullName}`,
    workType,
    targetDirectory,
    status: "pregatita",
    deliverables: deliverables.map(type => ({ id: `${id}-${type}`, type, label: deliverableLabels[type], state: "pending" })),
    history: [{ at: now, from: "date-validate", to: "pregatita", note: "Manifest pregătit în prototipul Dashboard v3" }],
    updatedAt: now,
    blockers: [],
  };
  state.works.unshift(work);
  saveState();
  byId("workDialog").close();
  navigate("works");
  toast("Lucrarea a fost pregătită; manifestul poate fi exportat");
});

window.addEventListener("hashchange", () => {
  const view = location.hash.replace("#/", "");
  if (view && view !== currentView) navigate(view);
});

const settings = loadSettings();
document.documentElement.dataset.density = settings.density === "Compact" ? "compact" : "comfortable";
navigate(currentView);
loadPersonsFromRegistry();
