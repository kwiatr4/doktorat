# Podsumowanie badania

## Tytuł
Digital phenotyping from wearables using AI characterizes psychiatric disorders and identifies genetic associations

## Cel pracy
Autorzy chcieli sprawdzić, czy dane z urządzeń ubieralnych (wearables) można wykorzystać jako obiektywne, ciągłe fenotypy cyfrowe do:
- lepszego wykrywania zaburzeń psychiatrycznych u młodzieży,
- zwiększenia mocy analiz genetycznych (GWAS) względem klasycznych, binarnych etykiet case-control.

## Dane i metodologia
- Kohorta: ABCD (Adolescent Brain Cognitive Development), 11,878 nastolatków (9-14 lat).
- Dane wearable (FitBit) dostępne dla 5,339 osób.
- Zbudowano dwa typy cech:
  - statyczne: 258 cech pochodnych ze statystyk sygnałów (m.in. tętno, sen, aktywność, METs),
  - dynamiczne: 48 kanałów szeregów czasowych po imputacji i przetwarzaniu.
- Modele AI:
  - XGBoost dla cech statycznych,
  - architektura typu Xception (CNN dla time series) dla cech dynamicznych.
- Zadania klasyfikacji:
  - ADHD vs zdrowe kontrole,
  - zaburzenia lękowe vs zdrowe kontrole.
- Interpretowalność: ablation + Grad-CAM (ważność cech i ważność czasowa).
- GWAS:
  - klasyczne case-control,
  - univariate i multivariate GWAS z wykorzystaniem ciągłych fenotypów cyfrowych / wearable combination score.

## Metoda krok po kroku
Metoda badania opierała się na połączeniu danych klinicznych, danych z wearables i genotypów.

1. **Zebranie danych**
  Autorzy wykorzystali kohortę ABCD, czyli dużą grupę nastolatków z danymi klinicznymi, demograficznymi, genetycznymi oraz zapisami z opasek FitBit.

2. **Przygotowanie cech z wearables**
  Z surowych sygnałów z opasek zbudowano dwa zestawy cech:
  - cechy statyczne, czyli podsumowania opisujące ogólny profil osoby,
  - cechy dynamiczne, czyli przetworzone szeregi czasowe pokazujące zmienność zachowania i fizjologii w czasie.
  Można to uprościć jako różnicę między „fotografią” a „filmem” funkcjonowania uczestnika.

3. **Klasyfikacja zaburzeń**
  Na tak przygotowanych danych uczono modele AI, które miały odróżniać osoby z ADHD lub zaburzeniami lękowymi od zdrowych kontroli. Cechy statyczne analizował XGBoost, a cechy dynamiczne model Xception, lepiej wykorzystujący informację czasową.

4. **Porównanie z baseline**
  Każdy model porównano z modelem bazowym opartym tylko na standardowych zmiennych klinicznych i demograficznych. Dzięki temu można było sprawdzić, czy wearables rzeczywiście dodają wartość diagnostyczną.

5. **Interpretacja modelu**
  Aby nie traktować AI jak czarnej skrzynki, autorzy sprawdzali ważność cech metodą ablation i analizowali znaczenie poszczególnych momentów czasu metodą Grad-CAM. Pozwoliło to wskazać, że szczególnie istotne były m.in. tętno, sen, aktywność i wzorce czasowe.

6. **Analiza genetyczna**
  Na końcu wykorzystano te cyfrowe fenotypy jako cechy w analizach GWAS. Zamiast klasycznej etykiety „chory/zdrowy” użyto też fenotypów ciągłych, co zwiększyło moc wykrywania sygnałów genetycznych.

7. **Ocena statystyczna**
  Jakość modeli oceniano przez AUROC i precision, a porównania z baseline testowano statystycznie. W pracy podkreślono, że modele dynamiczne dawały najlepsze wyniki.

## Najważniejsze wyniki
- Klasyfikacja ADHD:
  - baseline (kowariaty): AUROC ~0.83,
  - cechy statyczne: ~0.87,
  - cechy dynamiczne: ~0.89 (najlepszy wynik; istotna poprawa względem baseline).
- Klasyfikacja zaburzeń lękowych:
  - baseline: ~0.67,
  - statyczne: ~0.69,
  - dynamiczne: ~0.71 (również istotna poprawa).
- Cechy dynamiczne (czasowe) dawały najwyższą skuteczność, co sugeruje, że wzorce czasowe zachowania/fizjologii są kluczowe.
- W analizie genetycznej wykryto:
  - 16 istotnych loci,
  - 37 genów powiązanych psychiatrycznie (m.in. ELFN1, ADORA3).
- Autorzy raportują, że wearable-based GWAS miał większą moc detekcji niż tradycyjny GWAS case-control.

## Wnioski
- Fenotypowanie cyfrowe oparte o wearables i AI może lepiej opisywać heterogeniczne zaburzenia psychiatryczne niż kategorie diagnostyczne zero-jedynkowe.
- Użycie ciągłych fenotypów z wearables poprawia zarówno diagnostyczną predykcję, jak i odkrywanie sygnałów genetycznych.
- Podejście może wspierać medycynę precyzyjną w psychiatrii dzieci i młodzieży.

## Ograniczenia i uwagi
- Wyniki zależą od jakości i kompletności danych z urządzeń noszonych oraz od pipeline'u imputacji/przetwarzania.
- Przenaszalność do innych populacji, urządzeń i protokołów wymaga dalszej walidacji.
- Lepsza predykcja nie oznacza automatycznie przyczynowości biologicznej; konieczne są badania funkcjonalne.
