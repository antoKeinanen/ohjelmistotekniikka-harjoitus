# Ohjelmistotekniikka, harjoitustyö

## Dokumentaatio

- [Arkkitehtuuri](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Vaatimusmäärittely](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/changelog.md)
- [Työkirjanpito](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/työkirjanpito.md)

## Asennus ja käyttö

```bash
# Kloonaa projekti
git clone https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus.git

# Asenna riippuvuudet
poetry install

# Käynnistä sovellus
poetry run invoke start
```

### Yksikkötestaus

```bash
# Suorita testit
poetry run invoke test

# Testikattavuuden mittaaminen. Mittauksen tulokset tulevat htmlcov kansioon
poetry run invoke coverage-report
```

### Koodin automaattinen muotoilu

```bash
poetry run invoke format
```

### Koodin laadun varmistus

```bash
poetry run invoke lint
```
