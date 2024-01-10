# Grundlagen

---

## Was ist Kryptographie?

<section data-auto-animate>
</section>
<section data-auto-animate>
  <ul>
    <li>Kryptologie</li>
  </ul>
</section>
<section data-auto-animate>
  <ul>
    <li>Kryptologie
        <ul>
            <li> Kryptographie: Code machen
            <li> Kryptanalyse: Code brechen
        </ul>
    </li>
  </ul>
</section>

---

### Arten von Kryptographie

<section data-auto-animate>
  <ul>
    <li>Symmetrische Kryptographie
      <ul>
        <li>Beide Seiten haben den gleichen geheimen Schlüssel</li>
      </ul>
    </li>
    <li>Asymmetrische Kryptographie
      <ul>
        <li>Jede Person hat ein eigenes Schlüsselpaar bestehend aus einem geheimen und einem öffentlichen Schlüssel</li>
      </ul>
    </li>
</section>

<section data-auto-animate>
  <ul>
    <li>Symmetrische Kryptographie
      <ul>
        <li>Beide Seiten haben den gleichen geheimen Schlüssel</li>
      </ul>
    </li>
    <li>Asymmetrische Kryptographie
      <ul>
        <li>Jede Person hat ein eigenes Schlüsselpaar bestehend aus einem geheimen und einem öffentlichen Schlüssel</li>
      </ul>
    </li>
  <br/>
  <b>Welche Art würdet ihr verwenden um eine Festplatte zu verschlüsseln?</b>
</section>

---

### Ich habe doch nichts zu verbergen...

<section data-auto-animate>
</section>
<section data-auto-animate>
  <ul>
    <li>Sollen potenzielle Arbeitgeber*innen in der Lage sein private Informationen über euch herauszufinden?</li>
    <li>Was, wenn ihr ein Opfer von Stalking, Mobbing oder Spam werdet?</li>
    <li>Algorithmic Pricing</li>
    <li>Online-Banking (Verschlüsselung + Authentisierung)</li>
  </ul>
</section>

---

### Sicherheit = Safety + Security

- **Safety**: Das System muss zuverlässig unter "normalen" und "außergewöhnlichen" Bedingungen laufen
- **Security**: Das System muss in der Lage sein sich gegen böswillige Manipulation und Angriffe zu verteidigen

---

### Klartext

![Briefe mit Klartext](content/images/letter.jpg)

Für alle lesbar

---

### Chiffretext

![Grüne Matrix](content/images/ciphertext.jpg)

Unlesbar - Sieht aus wie etwas zufälliges

---

### Was ist eine Chiffre?

- Eine Chiffre wird definiert durch drei Mengen:
    - $P$ (Klartexte), $C$ (Chiffretexte), $K$ (Schlüssel)
- und drei effiziente Algorithmen:
    - $E: K \times P \rightarrow C$ (Verschlüsseln)
    - $D: K \times C \rightarrow P$ (Entschlüsseln)
    - $G: \ldots \rightarrow K$ (Schlüsselerzeugung)
- Für jeden Klartext $x \in P$ und jeden Schlüssel $k \in K$ gilt
$$D(k,(E(k,x)))=x$$

---

## Was ist besser?

1. Der Algorithmus bleibt geheim
2. Nur der Schlüssel bleibt geheim

--

### Kerkhoffs Prinzip

Ein System soll auch dann sicher sein, wenn die angreifende Person das System kennt, bis auf den verwendeten Schlüssel

---

#### Beispiel: Caesar Chiffre mit K=6

<section data-auto-animate>
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
  
U V W X Y Z <span style="color:green">A</span> B C D E F G H I J K L M N O P Q R S T

P = KRYPTOGRAPHIE  
C = ELSJNIALUJBCY
</section>
<section data-auto-animate>
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
  
U V W X Y Z <span style="color:green">A</span> B C D E F G H I J K L M N O P Q R S T

P = KRYPTOGRAPHIE  
C = ELSJNIALUJBCY  
  
Ist die Caesar Chiffre sicher?
</section>
<section data-auto-animate>
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
  
U V W X Y Z <span style="color:green">A</span> B C D E F G H I J K L M N O P Q R S T

P = KRYPTOGRAPHIE  
C = ELSJNIALUJBCY  
  
Ist die Caesar Chiffre sicher? -> Nein! Man kann sie mit simpler Statistik brechen :(
</section>

---

## Authentifizierung

Um die *Echtheit* von Nachrichten zu schützen, werden Message Authentication Codes (MACs) verwendet

- Schutz von Bank-Transaktionen vor Fälschung
- Schutz von Computerprogrammen vor Viren
- Schutz von Code vor
    - Veränderungen der Arbeitsweise
    - Denial of Service Angriffen
- ...

---

#### Was wenn wir Beides Kombinieren? - Authentisierte Verschlüsselung
Alice möchte ihrem Freund Bob Geld überweisen
- Sie will nicht, dass Andere die Details der Transaktion sehen (-> Verschlüsselung)
- Sie will nicht, dass die Transaktion verändert wird (-> Authentisierung)