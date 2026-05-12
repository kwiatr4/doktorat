# Plan badawczy – Doktorat wdrożeniowy 2026
## Smartfon-only monitoring rytmów okołodobowych: aplikacja w diagnostyce i monitorowaniu zaburzeń psychicznych

---

## 1. Kontekst i uzasadnienie projektu

### Problem kliniczny
- Tradycyjna diagnostyka zaburzeń psychicznych (zwłaszcza depresji) opiera się na subiektywnych narzędziach (PHQ-9, BDI-II, wywiady kliniczne), podatnych na błędy percepcji pacjenta i ograniczoną częstotliwość pomiaru.
- Lekarze pierwszego kontaktu błędnie klasyfikują depresję w ponad 50% przypadków.
- Brakuje obiektywnych, ciągłych i nieinwazyjnych metod monitorowania stanów związanych z zaburzeniami rytmów snu-czuwania i cykli okołodobowych.
- Rytmy okołodobowe są kluczowym biomarkerem w psychiatrii (depresja, zaburzenia dwubiegunowe, psychozy).

### Okazja technologiczna
- Smartfony zawierają biegle żyję czujniki (GPS, akcelerometr, mikrofon, ekran, dziennik aktywności, SMS/połączenia).
- Pasywny sensing mobilny (digital phenotyping) pozwala zbierać ciągłe dane behawioralne bez angażowania pacjenta.
- Algorytmy ML mogą integrować wielomodalny sygnał w interpretowalne biomarkery kliniczne.

### Punkt wyjścia badawczy
- Inspiracja: dwa artykuły wskazane przez Dr. Michała Ślęzaka (PORT Łukasiewicz), specjalistę od neurobiologicznych podstaw zaburzeń psychiatrycznych, zwłaszcza roli astrocytów i stresu przewlekłego.
- Wariant badania: **smartfon-only** bez opasek, bez dodatkowych urządzeń noszonych.
- Aplikacja: bezpośrednie wsparcie psychologów i psychiatrów w diagnostyce i monitorowaniu rytmów okołodobowych.

---

## 2. Cele główne i hipotezy

### Cel główny
Opracowanie i walidacja metody oceny rytmów okołodobowych pacjentów na podstawie pasywnych danych ze smartfona, która będzie wspierać psychologów i psychiatrów w diagnozie oraz monitorowaniu zaburzeń psychiatrycznych związanych z zaburzeniami snu i rytmów dobowych.

### Cele szczegółowe
1. Opracować algorytm ekstrakcji i integracji biomarkerów rytmu dobowego z co najmniej 4 strumieni pasywnych (mobilność, sen, użycie telefonu, aktywność).
2. Walidować opracowaną metodę w populacji min. 100 uczestników z różnymi profili klinicznymi (zdrowotni, subsyndromalni, depresja, zaburzenia dwubiegunowe).
3. Ocenić użyteczność kliniczną i akceptowalność narzędzia u psychologów klinicznych (n≥15).
4. Przygotować prototyp aplikacji mobilnej do praktyki klinicznej.

### Hipotezy główne
1. **H1 (wdrożeniowa):** Integracja pasywnych danych behawioralnych ze smartfona (rytmy mobilności, snu, użycia telefonu, aktywności) będzie pozwalać na wiarygodną (r≥0.70) ocenę zaburzeń rytmu dobowego w zaburzeniach psychicznych, porównując się z klasycznymi miarami klinicznymi (PHQ-9, skale snu).
2. **H2 (naukowa):** Profile behawioralne „smartfon-only" będą rozróżniać grupy kliniczne (zdrowe vs. subsyndromalne vs. depresja) z dokładnością >75%, zamiast używania sztywnych progów wartości.
3. **H3 (praktyczna):** Psycholodzy kliniczni ocenią wynik opracowanej metody jako użyteczny w co najmniej 60% przypadków i będą deklarować wartość dodaną w procesie diagnostycznym/terapeutycznym.

---

## 3. Dane biometryczne i behawioralne ze smartfona

### Zdolne do ekstrakcji sygnały (pasywny sensing)

| Typ danych | Co mierzymy | Potencjalne biomarkery rytmu dobowego | Ryzyko pomiarowe |
|-----------|------------|--------------------------------------|-----------------|
| 📍 **Mobilność (GPS)** | Liczba lokalizacji, czas w domu, entropia tras, regularność | Hipomobilność, więcej czasu w domu, zaburzenie rytmu spatial | Wymagana zgoda użytkownika, zużycie baterii, niedokładność w budynkach |
| 💤 **Wzorce snu (akcelerometr, screen-off)** | Czas położenia/wstania, regularność, czas w łóżku | Nieregularny sen, wcześne przebudzenia, fragmentacja | Akcelerometr nie rozróżnia snu od leżenia, zależność od ruchu |
| 📱 **Użycie telefonu** | Screen time, czas w social mediach, wzorce nocne | Nocna hiperstymulacja, zaburzenie snu-czuwania | Self-selection bias, zmienność indywidualna |
| 🎙️ **Mowa/Analiza głosu** | Częstotliwość rozmów, czas rozmów, liczba kontaktów | Izolacja społeczna, zmienność stresu w głosie | Wymaga nagrywania, prywatność użytkownika |
| 🏃 **Aktywność fizyczna (akcelerometr, kroki)** | Kroki, poziom ruchu, czas siedzenia | Niższa aktywność = zaburzenia rytmu | Zależność od warunków pogodowych, noszenia telefonu |
| ⌨️ **Dynamika pisania** | Szybkość pisania, opóźnienia, backspace rate | Spowolnienie psychomotoryczne | Mała liczba interakcji SMS u starszych, komunikatorów |

### Priorytet dla projektu doktoratu
- **Tier 1 (obowiązkowe):** GPS, akcelerometr (sen + aktywność), screen-off
- **Tier 2 (opcjonalne):** mowa, dynamika pisania, social media
- Razem **minimum 4-6 strumieni** do integracji w algorytmie.

---

## 4. Metodologia badawcza – 4 fazy

### FAZA 1: Specyfikacja i przygotowanie (miesiące 0-2)
**Działania:**
- Warsztaty z psychologami klinicznymi (n≥10) w celu zdefiniowania wymagań funkcjonalnych.
- Opracowanie protokołu badań, warunków etycznych, zgodności RODO.
- Wybór i szkolenie w zakresie ram teoretycznych i artykułów referencyjnych.

**Rezultat:**
- Dokument specyfikacji wymagań (funkcjonalności, metryki kliniczne, kryteria użyteczności).
- Pozwolenie etyczne i zgoda IRB.

---

### FAZA 2: Budowa prototypu i zbieranie danych (miesiące 3-14)
**Działania:**
- Opracowanie aplikacji mobilnej do pasywnego zbierania 4-6 strumieni danych (Android + iOS, jeśli to możliwe).
- Rekrutacja uczestników (n≥100; idealne: n=30 zdrowych, n=30 depresja kliniczne, n=40 subsyndromalne/inne zaburzenia).
- Czas obserwacji: minimum 12 tygodni na uczestnika (dla pełnego cyklu rytmu dobowego).
- Równoległa walidacja kliniczna: PHQ-9, HAM-D, Pittsburg Sleep Quality Index (PSQI), Karolinska Sleepiness Scale (KSS).
- Zbieranie danych demograficznych, diagnostycznych, psychofarmakologicznych.

**Rezultat:**
- Multimodalny zbiór danych: 6 strumieni pasywnych × 100 uczestników × 12 tygodni = **~80 000 punkt danych**.
- Zestawienie wyników klinicznych (PHQ-9, HAM-D, PSQI) dla każdego uczestnika.

---

### FAZA 3: Algorytmika i walidacja metodologiczna (miesiące 15-24)
**Działania:**
- Ekstrakcja biomarkerów z każdego strumienia (feature engineering).
- Normalizacja i transformacja do porównywalnych skal.
- Opracowanie modelu ML integrującego wielomodalny sygnał (np. ensemble, random forest, gradient boosting, ewentualnie głębokie sieci).
- Personalizacja: każdy pacjent otrzymuje indywidualny profil behawioralny zamiast sztywnych progów.
- Walidacja krzyżowa (k-fold), test na zestawie holdout.
- Ocena wydajności: czułość, specyficzność, AUC-ROC, korelacja z miarami klinicznymi (r≥0.70).

**Rezultat:**
- Algorytm predykcyjny zbijający wielomodalny sygnał w **interpretowalne wskaźniki rytmu dobowego**.
- Raport techniczny z wydajnością modelu.

---

### FAZA 4: Ewaluacja kliniczna i pilotaż (miesiące 25-36)
**Działania:**
- Pilotaż prototypu wśród psychologów klinicznych (n≥15) w warunkach zbliżonych do praktyki.
- Podanie się testom użyteczności (SUS – System Usability Scale, TAM – Technology Acceptance Model).
- Ocena wpływu na decyzje diagnostyczne/terapeutyczne (ankieta post-sesyjna, zmiana planu leczenia).
- Zbieranie informacji zwrotnej iteracyjnej, refinement algorytmu.

**Rezultat:**
- Raport efektywności klinicznej (SUS score, akceptacja, wartość dodana).
- Wersja prototypu gotowa do wdrożenia.

---

## 5. Plan wdrożenia i partnerstwo

### Podmiot wdrażający
**Startup + PORT Łukasiewicz**
- Startup: bieżąca rozbudowa aplikacji, integracja z badaniami doktorskimi.
- PORT Łukasiewicz: dostęp do infrastruktury badawczej, sieci psychologów klinicznych, walidacja laboratoryjno-kliniczna.

### Produkt wdrożenia
- **Miesiąc 12:** Prototyp aplikacji z algorytmem do wewnętrznych testów.
- **Miesiąc 24:** Wersja 1.0 gotowa do pilotażu u psychologów (min. 3 ośrodki kliniczne).
- **Miesiąc 36:** Aplikacja pełnoprawnie wdrożona, gotowa do pierwszych pacjentów (z odpowiednimi certyfikacjami, jeśli wymagane).

### Eksploatacja po doktoracie
- Aplikacja będzie dostępna psychologom/psychiatrom jako narzędzie wspierające (bez zastępowania klinicysty).
- Możliwy model: aplikacja w otwartym dostępie + wersja premium dla ośrodków klinicznych.
- Dokumentacja naukowa: publikacje w czasopismach psychiatrycznych i bioinformatycznych.

---

## 6. Ryzyka i ich mitygacja

| Ryzyko | Waga | Mitygacja |
|--------|------|-----------|
| Niska rekrutacja uczestników (n<50) | Wysoka | Wieloośrodkowa rekrutacja, informacja zwrotna finansowa (do 200 PLN/os.), kooperacja ośrodków klinicznych |
| Brak danych z powodu rezygnacji użytkownika | Średnia | Częste remindery w aplikacji, minimalizacja obciążenia użytkownika, przystępy do wyjścia |
| Niedokładność GPS/akcelerometru w pomieszczeniach | Średnia | Hybrydowe podejście: GPS + WiFi localization, w analizie zwrócić uwagę na sygnał słaby |
| Wymagania RODO / szyfrowanie danych | Wysoka | Szyfrowanie end-to-end, anonimizacja ID, przechowywanie na serwerze zgodnym z RODO (UE) |
| Brak zgody etycznej / regulacyjne opóźnienia | Wysoka | Wczesne rozmowy z IRB, przygotowanie dokumentacji już w fazie 1 |
| Niska akceptacja psychologów (SUS<68/100) | Średnia | Iteracyjny design, feedback od klinicystów już w fazie 2, zaangażowanie użytkowników |
| Słaba wydajność algorytmu (r<0.70) | Średnia | Eksploracja różnych architektur ML, feature engineering na podstawie domeny (psychiatria), w razie potrzeby: zaangażowanie eksperta ds. ML |

---

## 7. Wymogi programu „Doktorat wdrożeniowy 2026"

### Spełnione kryteria

✅ **Wdrożeniowy charakter projektu (TAK/NIE)** – Obowiązkowe  
- Aplikacja będzie wdrożona u psychologów klinicznych, ma jasny plan komercjalizacji i wpływ na praktykę kliniczną.

✅ **Powiązanie ze startupem / podmiotem społeczno-gospodarczym**  
- Startup + PORT Łukasiewicz jako podmiot współpracujący, doktorant zatrudniony na etat w startupiie/PORT.

✅ **Znaczenie naukowe**  
- Pierwszy projekt integrujący wielomodalny passive sensing ze smartfona w osadzeniu psychiatrycznym; personalizowana ocena rytmu dobowego.

✅ **Znaczenie dla gospodarki/społeczeństwa**  
- Zaburzenia psychiatryczne to koszt €1 tryliona rocznie dla UE; narzędzie mogą poprawić diagnostykę i zmniejszyć obciążenie zdrowotne.

✅ **Wymagania formalne**  
- Doktorant zatrudniony w startupiie/PORT z umową o pracę (pełny etat) od 1 października 2026 r. (do spełnienia).
- Opiekun pomocniczy wyznaczony po stronie podmiotu współpracującego (do spełnienia).
- Promotor akademicki ze szkoły doktorskiej (do spełnienia).

### Wskaźniki sukcesu (za 36 miesięcy)

| Wymiar | Metryka | Cel |
|--------|---------|-----|
| Użyteczność kliniczna | SUS score | ≥ 68/100 |
| Akceptacja | TAM | ≥ 4/5 |
| Zgodność z oceną kliniczną | Korelacja r | ≥ 0.70 |
| Wpływ na decyzje | % psychologów deklarujących wartość | ≥ 60% |
| Wdrożenie | Liczba ośrodków klinicznych | ≥ 3 |
| Publikacje | Artykuły w czasopismach | ≥ 2 |

---

## 8. Harmonogram roboczy (36 miesięcy)

| Semestr | Aktywności naukowe | Aktywności wdrożeniowe |
|---------|-------------------|----------------------|
| **1–2** | Przegląd literatury, specyfikacja wymagań, opracowanie protokołu badań | Prototypowanie aplikacji, testy alfa |
| **3–4** | Weryfikacja opasu, przygotowanie do zbierania danych, szkolenia zespołu | Integracja funkcjonalności do aplikacji, testy beta |
| **5–6** | Zbieranie danych (100 uczestników, 12 tygodni) | Rafinacja aplikacji na podstawie feedback, przygotowanie do pilotażu |
| **7–8** | Analiza danych, ekstrakcja biomarkerów, feature engineering | Wdrożenie pilotażu u 3 psychologów, zbieranie feedback |
| **9–10** | Budowa modelu ML, walidacja krzyżowa, testy wydajności | Iteracyjne ulepszenia algorytmu, pierwsza publikacja |
| **11–12** | Ewaluacja kliniczna (15 psychologów), raporty finalne | Przygotowanie do wdrożenia pełnoprawnego, druga publikacja, planowanie komercjalizacji |

---

## 9. Edukacja doktoranta

### Umiejętności naukowe
- Metodologia badań psychiatrycznych i digital phenotyping.
- Projektowanie studii klinicznych (randomizacja, kontrola, walidacja).
- Statystyka i analiza wielomodalnych danych.
- Machine Learning i interpretowalność algorytmów w medycynie.

### Umiejętności wdrożeniowe
- Zarządzanie projektem IT i współpraca ze startup'em.
- Regulacje medyczne (RODO, CE dla oprogramowania medycznego, jeśli wymagane).
- Komunikacja naukowa dla klinicystów i pacjentów.
- Prezentacja wyników na konferencjach psychiatrycznych.

### Wsparcie szkoły doktorskiej
- Szkoła zapewnia szkolenia z metodologii badawczej.
- Promotor akademicki wspiera aspekt naukowy i publikacje.
- Opiekun pomocniczy (PORT) wspiera aspekt wdrożeniowy i praktyki klinicznej.

---

## 10. Linki do artykułów referencyjnych

1. **[Artykuł 1 od Dr. Ślęzaka]** – Neurobiologiczne podstawy zaburzeń rytmu dobowego w psychiatrii (do uzupełnienia).
2. **[Artykuł 2 od Dr. Ślęzaka]** – Digital phenotyping w ocenie zaburzeń psychicznych (do uzupełnienia).
3. Shen et al. (2025) – Passive Sensing for Mental Health Monitoring Using ML. *JMIR*. Scoping review, 42 studia, 2015–2025.
4. De Angel et al. (2022); Torous et al. (2016) – Foundational works on digital phenotyping framework.

---

## 11. Kontakt i role

| Rola | Osoba | Afiliacja |
|------|-------|----------|
| Doktorant | [Ty] | Szkoła doktorska (do ustalenia) + startup |
| Promotor akademicki | [Do ustalenia] | Szkoła doktorska |
| Opiekun pomocniczy | [Do ustalenia] | PORT Łukasiewicz / startup |
| Mentor biznesowy | [Do ustalenia] | Startup |

---

## 12. Notatka: następne kroki

1. ✅ Zatwierdzić temat z Dr. Ślęzakiem (PORT).
2. ❌ **Znaleźć szkołę doktorską i promotora akademickiego** ← PRIORYTET
3. ❌ Potwierdzić opiekuna pomocniczego i umowę o pracę w startupiie.
4. ❌ Sporządzić pełny wniosek do części I (11 maja – 12 czerwca 2026 r.).
5. ❌ Przeprowadzić rekrutację doktoranta do szkoły doktorskiej.
6. ❌ Złożyć część II wniosku (do 22 września 2026 r.).

---

*Plan opracowany: maj 2026*
*Ostatnia aktualizacja: maj 12, 2026*
