from generate_matrita_datei_de_nastere import build_html_component, build_svg, compact_geometry


def main() -> None:
    _, daniel = build_svg("Birsan Daniel Robert", "19.02.1998")
    assert (daniel["n1"], daniel["n2"], daniel["n3"], daniel["n4"]) == (39, 12, 37, 10)
    assert daniel["sequence"] == "1902199839123710"
    daniel_component, _ = build_html_component("Birsan Daniel Robert", "19.02.1998")
    assert daniel_component.count('class="matrix-cell ') == 9
    assert "1111" in daniel_component and "9999" in daniel_component

    andreea_component, andreea = build_html_component("Roman Andreea Maria", "12.01.1998")
    assert (andreea["n1"], andreea["n2"], andreea["n3"], andreea["n4"]) == (31, 4, 29, 11)
    assert andreea["sequence"] == "120119983142911"
    assert andreea_component.count('class="matrix-cell ') == 9
    assert 'aria-label="hexagramă"' in andreea_component
    hexagram, _ = compact_geometry(6)
    assert 'points="20,5 30,22 10,22"' in hexagram
    assert 'points="20,27 10,10 30,10"' in hexagram
    print("Regresii G-002 Daniel si Andreea: OK")


if __name__ == "__main__":
    main()
