
# Aplikacja Django do wgrywania sprawozdań PDF/ DOCX / DOC

Projekt umożliwiający wgranie sprawozdania przez studenta na dysk w formacie .pdf, .doc, .docx. Student uzupełnia swoje dane w formularzu i wgrywa plik. Po wysłaniu plik zostaje zaspisany na dysku.

## Uruchomienie
W pliku ```Site_Config.py``` do zmiennej ```files_destination``` należy podać ścieżkę do folderu do którego mają być przesłane pliki. Jeżeli zmienna ta będzie pusta, wówczas plik zostanie przesłany do folderu ```sprawozdania/pliki_sprawozdania``` w folderze projektu. W obydwu przypadkach program sprawdza czy folder już istnieje, w przeciwnym razie go utworzy.

```python
files_destination = "{ścieżka do folderu}"
```

Instalujemy biblioteke do virtual env

```py -m pip install virtualenv```

Tworzymy virtual env

```py -m virtualenv venv```

Uruchamiamy virtual env

```.\venv\Scripts\activate```

Instalujemy Django

```py -m pip install django```

Wchodzimy w katalog projektu i uruchamiamy projekt
```cd sprawozdania```

```py .\manage.py runserver```

Pod adresem ```http://127.0.0.1:8000``` dostępny jest formularz do wysyłania sprawozdań.