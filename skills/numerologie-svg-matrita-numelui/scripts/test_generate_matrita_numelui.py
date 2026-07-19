from generate_matrita_numelui import build_svg, geometry


def main() -> None:
    svg, meta = build_svg("Birsan Daniel Robert", "19.02.1998")
    assert meta["counts"][9] == 5
    assert meta["date_counts"][9] == 4
    assert geometry(meta["counts"][9], 20, 20)[1] == "pentagrama"
    assert "data 9999" in svg
    assert "99999" in svg
    comparison = meta["comparison"]
    assert comparison["supported"] == [1, 2, 3, 9]
    assert comparison["excess_name"] == {5: 4, 6: 2}
    assert comparison["missing_name"] == [7, 8]
    assert comparison["name_potential"] == [4, 5, 6]
    assert comparison["active_vectors_date"] == ["123, Energie", "789, Creativitate"]
    assert comparison["active_vectors_name"] == ["123, Energie", "456, Vointa", "369, Bunastare materiala", "159, Cariera"]
    print("Regresie Daniel casuta 9: OK (99999 -> pentagrama)")


if __name__ == "__main__":
    main()
