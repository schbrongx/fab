# FAB - Form Autofill Bookmarklet-Generator

Willkommen zu **FAB**! Diese Anwendung soll Ihnen dabei helfen, Formulare im Web automatisiert auszufüllen. Die Idee ist, Ihnen Zeit und Mühe zu sparen, indem immer wiederkehrende Formularfelder mit minimalem Aufwand ausgefüllt werden.

## Funktionsweise
**FAB** erzeugt ein Bookmarklet (ein kleines JavaScript-Programm, das Sie als Lesezeichen in Ihrem Browser speichern können). Es hilft Ihnen, Formulare in verschiedenen Webanwendungen automatisch auszufüllen, indem es einmal hinterlegte Daten in die entsprechenden Felder einfügt.
In jeder Zeile kann ein frei gewählter Name, der (technische) Feldname des Formularfelds und ein auszufüllender Wert angegeben werden. Mit den kleinen Icons
am Ende der Zeile, kann man die Zeile leeren, die Zeile löschen, eine Zeile anfügen oder die Zeile verschieben.

Sobald man alle Formularfelder, die man ausfüllen lassen möchte, zusammengestellt hat, kann man ein "Bookmarklet generieren" und dieses generierte Bookmarklet
dann jederzeit im Browser benutzen um Formularfelder auszufüllen.

## Hilfs-Bookmarklet
Das Bookmarklet im Hilfemenü hilft dabei, die Namen der Felder auf einer Webseite zu identifizieren. Diese Informationen können dann zur Konfiguration des Programms verwendet werden, um die spezifischen Felder der Webseite automatisiert auszufüllen.
Für Felder die mehrere vordefinierte Werte annehmen können, werden auch die vordefinierten Werte angezeit, wenn möglich.
Das Bookmarklet kann mehrmals betätigt werden um die Feldanzeige an- und auszuschalten.

## Installation eines Bookmarklets
1. **Erzeugung des Bookmarklets**: Entweder das Bookmarklet mit dem Knopf "Bookmarklet generieren" erzeugen und mit dem Kopier-Knopf in die Zwischenablage
kopieren, oder das Bookmarklet aus dem Hilfemenü mit dem Kopier-Knopf in die Zwischenablage kopieren.

2. **Hinzufügen des Bookmarklets zu Ihrem Browser**:
   
   ### Microsoft Edge
   - Öffnen Sie die Favoritenleiste („Strg+Umschalttaste+B“).
   - Ziehen Sie das JavaScript Bookmarklet in die Leiste, oder erstellen Sie ein neues Lesezeichen mit dem Code des Bookmarklets als URL.

   ### Mozilla Firefox
   - Drücken Sie „Strg+Umschalttaste+B“, um die Lesezeichenleiste einzublenden.
   - Klicken Sie auf "Neues Lesezeichen erstellen" und fügen Sie den JavaScript-Code als URL hinzu.

   ### Google Chrome
   - Drücken Sie „Strg+Umschalttaste+B“, um die Lesezeichenleiste sichtbar zu machen.
   - Ziehen Sie das Bookmarklet in die Leiste oder erstellen Sie ein neues Lesezeichen mit dem Code als URL.

## Verwendung des Bookmarklets
Nachdem das Bookmarklet in Ihrem Browser eingerichtet wurde, können Sie es mit einem Klick darauf aktivieren, genau wie ein normales Lesezeichen. Es wird dann jedoch keine hinterlegte Seite geöffnet, sondern die Funktion des Bookmarklets ausgeführt.

* Das Hilfs-Bookmarklet wird die Formularfelder der aktuellen Webseite untersuchen und die Feldnamen anzeigen. Diese Namen können verwendet werden, um die Konfigurationsdatei des **FAB**-Programms anzupassen, sodass die richtigen Informationen an die richtigen Stellen im Formular eingetragen werden.

* Das generierte Bookmarklet wird die Felder des Formulars auf der aktuellen Webseite ausfüllen, wenn alles richtig konfiguriert ist.

### Formular automatisch ausfüllen
1. **Identifizierung der Formularfelder**: Klicken Sie auf das Hilfs-Bookmarklet, um die Namen der Formularfelder anzuzeigen.
2. **Konfiguration des Programms**: Nutzen Sie die identifizierten Feldnamen, um **FAB** zu konfigurieren. Dies ermöglicht dem Programm, spezifische Felder automatisch mit Ihren bereitgestellten Daten zu füllen.
3. **Automatisches Ausfüllen**: Nachdem die Konfiguration vorgenommen wurde, können Sie das Autofill-Bookmarklet verwenden, um das Formular automatisch auszufüllen.

## Releases herunterladen
Die neuesten Versionen können direkt auf der [Releases-Seite](https://github.com/schbrongx/form.autofiller/releases) des GitHub-Repositories heruntergeladen werden. Hier finden Sie alle Veröffentlichungen mit entsprechenden Versionshinweisen, Installationshinweisen und nützlichen Informationen. 

## Fehler melden und Kontakt
Sollten Ihnen Fehler oder Verbesserungsvorschläge auffallen, können Sie diese direkt über den [Issue-Tracker](https://github.com/schbrongx/form.autofiller/issues) auf GitHub melden. Alternativ können Sie mich auch über das GitHub-Profil [schbrongx](https://github.com/schbrongx) kontaktieren.

Vielen Dank für die Nutzung von **FAB**! Wir freuen uns auf Ihr Feedback und Ihre Verbesserungsvorschläge.

