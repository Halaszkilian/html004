import pytest
from bs4 import BeautifulSoup

def test_html_file_exists():
    """
    Ellenőrzi, hogy a index.html fájl létezik-e.
    """
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            assert True
    except FileNotFoundError:
        assert False, "Az index.html fájl nem létezik."

def test_html_lang_attribute():
    """
    Ellenőrzi, hogy a HTML dokumentum nyelvi attribútuma helyesen van-e beállítva.
    """
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        html_tag = soup.find("html")
        assert html_tag is not None, "A html tag hiányzik."
        assert html_tag.get("lang") == "hu", "A nyelvi attribútum nincs 'hu'-ra állítva."

def test_title_element():
    """
    Ellenőrzi, hogy a title elem 'HP-UX'-ra van-e állítva.
    """
    with open("index.html", "r", encoding="utf-8") as f:
         soup = BeautifulSoup(f, "html.parser")
         title_tag = soup.find("title")
         assert title_tag is not None, "A title tag hiányzik."
         assert title_tag.text == "HP-UX", "A title nem 'HP-UX'-ra van állítva."

def test_h1_element():
    """
    Ellenőrzi, hogy az h1 elem jelen van-e és a tartalma "HP-UX".
    """
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        h1_tag = soup.find("h1")
        assert h1_tag is not None, "Az h1 tag hiányzik."
        assert h1_tag.text == "HP-UX", "Az h1 tag tartalma nem megfelelő."

def test_paragraph_elements():
    """
    Ellenőrzi, hogy két bekezdés van-e (az első és a második a hpux.txt szövege).
    """
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        paragraphs = soup.find_all("p")
        assert len(paragraphs) == 2, "Két bekezdés elemnek kell lennie."

def test_paragraph_with_supported_platforms():
    """
    Ellenőrzi, hogy a 'Támogatott platformok' bekezdés helyesen van-e formázva.
    """
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        paragraphs = soup.find_all("p")
        # Ellenőrizzük, hogy a platformok megfelelően szerepelnek egy bekezdésben
        assert "Támogatott platformok:" in paragraphs[1].text, "A 'Támogatott platformok' nem szerepel megfelelően."

def test_abbr_and_mark_tags():
    """
    Ellenőrzi, hogy a 'HP 9000' és 'HP Integral PC' megfelelően van-e tagolva.
    """
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        p_tag = soup.find_all("p")[1]
        abbr_tag = p_tag.find("abbr")
        mark_tag = p_tag.find("mark")
        assert abbr_tag is not None, "A 'HP 9000' rövidítés hiányzik."
        assert abbr_tag.text == "HP 9000", "A 'HP 9000' rövidítés szövege nem megfelelő."
        assert mark_tag is not None, "A 'HP Integral PC' kiemelés hiányzik."
        assert mark_tag.text == "HP Integral PC", "A 'HP Integral PC' kiemelés szövege nem megfelelő."

def test_html_comment():
    """
    Ellenőrzi, hogy a "Név: [A te neved] Dátum: [aktuális dátum]" komment létezik-e a HTML forráskódban.
    """
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
        assert "<!-- Név:" in content, "A név komment hiányzik a HTML kódból."
        assert "<!-- Dátum:" in content, "A dátum komment hiányzik a HTML kódból."

if __name__ == "__main__":
    pytest.main()
