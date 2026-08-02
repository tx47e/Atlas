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

const seed = {
  persons: [
    { id: "person-demo-1", fullName: "Andrei Popescu", birthDate: "1985-05-17", notes: "Profil demonstrativ" },
    { id: "person-demo-2", fullName: "Maria Ionescu", birthDate: "1992-11-03", notes: "Profil demonstrativ" },
    { id: "person-demo-3", fullName: "Elena M.", birthDate: "1990-08-26", notes: "Profil demonstrativ" },
  ],
  works: [
    createSeedWork("work-demo-1", "person-demo-1", "Analiză numerologică — Andrei Popescu", "Analiză numerologică", "in-lucru", 3, "2026-07-27T09:25:00+03:00"),
    createSeedWork("work-demo-2", "person-demo-2", "Matricea Destinului — Maria Ionescu", "Lucrare scurtă", "in-revizie", 4, "2026-07-26T15:10:00+03:00"),
    createSeedWork("work-demo-3", "person-demo-3", "Prognoză anuală — Elena M.", "Analiză numerologică", "pregatita", 1, "2026-07-25T11:40:00+03:00"),
  ],
};

function createSeedWork(id, personId, title, workType, status, completed, updatedAt) {
  return {
    id,
    personId,
    title,
    workType,
    targetDirectory: `output/lucrari/${id}`,
    status,
    deliverables: Object.keys(deliverableLabels).map((type, index) => ({
      id: `${id}-${type}`,
      type,
      label: deliverableLabels[type],
      state: index < completed ? "done" : index === completed ? "active" : "pending",
    })),
    history: [{ at: updatedAt, from: "pregatita", to: status, note: "Stare demonstrativă" }],
    updatedAt,
    blockers: [],
  };
}

let state = loadState();
let currentView = location.hash.replace("#/", "") || "dashboard";
if (!viewTitles[currentView]) currentView = "dashboard";
let activeWorkFilter = "toate";

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
    if (stored?.persons && stored?.works) return stored;
  } catch {}
  return clone(seed);
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
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
  byId("breadcrumb").textContent = `Atlas / ${viewTitles[view]}`;
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
          <option value="">Se încarcă lista...</option>
        </select>
        <button id="calculatorHostLoadBtn" class="secondary-button" type="button">Încarcă</button>
        <button id="calculatorHostNewBtn" class="secondary-button" type="button">Persoană nouă</button>
      </div>
      <iframe
        class="calculator-frame"
        src="calculator.html"
        title="Calculator numerologic Atlas"
        loading="eager"
        scrolling="yes"
      ></iframe>
    </section>
  `;
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
      <article class="card feature-card" data-category="Tarot"><img class="vault-art" src="assets/vault-card-tarot-hd.svg" alt="Trei cărți de Tarot ilustrate, cu Arcana 0 — The Fool în centru"><h3>Tarot</h3><p>Arcane și corespondențe</p></article>
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

  const connect = () => {
    const innerDocument = frame.contentDocument;
    const innerSelect = innerDocument?.getElementById("personSelect");
    const innerLoad = innerDocument?.getElementById("loadPersonBtn");
    const innerNew = innerDocument?.getElementById("newPersonBtn");
    if (!innerSelect || !innerLoad || !innerNew) return false;

    const syncOptions = () => {
      const signature = [...innerSelect.options].map(option => `${option.value}:${option.textContent}`).join("|");
      if (hostSelect.dataset.optionsSignature !== signature) {
        hostSelect.innerHTML = [...innerSelect.options]
          .map(option => `<option value="${escapeHtml(option.value)}">${escapeHtml(option.textContent)}</option>`)
          .join("");
        hostSelect.dataset.optionsSignature = signature;
      }
      hostSelect.value = innerSelect.value;
    };

    syncOptions();
    innerSelect.addEventListener("change", syncOptions);
    hostSelect.addEventListener("change", () => {
      innerSelect.value = hostSelect.value;
      innerSelect.dispatchEvent(new Event("change", { bubbles: true }));
    });
    hostLoad.addEventListener("click", () => innerLoad.click());
    hostNew.addEventListener("click", () => innerNew.click());

    const optionsObserver = new MutationObserver(syncOptions);
    optionsObserver.observe(innerSelect, { childList: true, subtree: true, attributes: true });
    return true;
  };

  frame.addEventListener("load", connect, { once: true });
  if (frame.contentDocument?.readyState === "complete") connect();
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
byId("newWorkBtn").addEventListener("click", openWorkDialog);
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
    person = { id: `person-${crypto.randomUUID()}`, fullName, birthDate, notes: "" };
    state.persons.push(person);
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
