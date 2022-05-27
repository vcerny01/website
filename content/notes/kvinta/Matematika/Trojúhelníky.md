---
date: 2022-05-04
series: Matematika
math: true
---

## Základní vlastnosti trojúhelníku
- [[assets/vlastnosti-trojuhelniku.pdf|PDF]]

## Obsah trojúhelníku
### 1. Obecný vzorec
- Obsah trojúhelníku ($S$) spočítáme tak, že velikost jedné strany vynásobíme velikostí příslušné výšky (tím vznikne kosodelník nebo něco takového) a vydělíme dvěma (jsme na trojúhelníku)

$$S = \frac{a \cdot v_a}{2} = \frac{b \cdot v_b}{2} = \frac{c \cdot v_c}{2}$$

### 2. Heronův vzorec
- V případě, že známe velikost všech tří stran $a$, $b$, $c$ trojúhelníku $ABC$, jeho obsah můžeme spočítat pomocí vztahu:

$$S=\sqrt{s \cdot (s-a) \cdot (s-b) \cdot (s-c)}$$

- Kde $s=\frac{a+b+c}{2}$

### 3. Pomocí sinu úhlu
- V případě, že v trojúhelníku známe délku dvou stran a velikost úhlu jimi sevřeného, pak můžeme obsah tohoto trojúhelníku vypočítat pomocí jednoho ze vztahů:
	- $\large{S=\frac{1}{2} \cdot b \cdot c \cdot sin \alpha}$
	- $\large{S=\frac{1}{2} \cdot a \cdot c \cdot sin \beta}$
	- $\large{S=\frac{1}{2} \cdot a \cdot b \cdot sin \gamma}$

### 4. Obsah pravoúhlého trojúhelníku
- Pro obsah pravoúhlého trojúhelníku ABC, kde c je přepona a a, b jsou odvěsny, platí:

$$S=\frac{a \cdot b}{2}$$

### Další vzorce pro výpočet obsahu trojúhelníku
- (nepovinné)
- 1. **Rovnostranný trojúhelník**
	- Obsah rovnostranného trojúhelníku $a$ můžeme spočítat podle vztahu:

$$S=\frac{\sqrt{3}}{4}a^2$$

- 2. **Pomocí poloměru kružnice trojúhelníku opsané**

$$S=\frac{abc}{4r}$$

- 3. **Pomocí poloměru kružnice trojúhelníku vepsané**

$$S=r \cdot \frac{a+b+c}{2}$$


## Shodnost trojúhelníků
- = Dva trojúhelníky jsou shodné, jestliže přemístěním jednoho trojúhelníku na druhý oba splynou

### Věta sss
- Jestliže se dva trojúhelníky shodují v délkách všech tří stran, pak jsou shodné

### Věta sus
- Jestliže se dva trojúhelníky shodují v délkách dvou stran a v úhlu jimi sevřeném, pak jsou shodné

### Věta Ssu
- Jestliže se dva trojúhelníky shodují v délkách dvou stran a v úhlu proti delší z nich, pak jsou shodné

## Podobnost trojúhelníků
- $\triangle ABC$ je podobný $\triangle KLM$,  jestliže existuje číslo $k$ tak, že:
	- $|KL| = k \cdot |AB|$
	- $|LM| = k \cdot |BC|$
	- $|KM| = k \cdot |AC|$
- $k$ je poměr (koeficient) podobnosti $\triangle ABC$ a $\triangle KLM$
	- $k > 1$  => **zvětšení**
	- $k = 1$ => **shodnost**
	- $k < 1$  => **zmenšení**
- Platí věty uu, sus, Ssu o podobnosti trojúhelníku
## Goniometrické funkce

$$sin(\alpha) = \frac{\text{délka protilehlé odvěsny}}{\text{délka přepony}}$$

$$cos(\alpha) = \frac{\text{délka přilehlé odvěsny}}{\text{délka přepony}}$$

$$tan(\alpha) = \frac{\text{délka protilehlé odvěsny}}{\text{délka přilehlé odvěsny}}$$

- $cot$ je v podstatě jen převrácený tangens.



|            | $sin$                | $cos$                | $tan$                | $cot$                |
| ---------- | -------------------- | -------------------- | -------------------- | -------------------- |
| $0^\circ$  | $0$                  | $1$                  | $0$                  | $\times$             |
| $30^\circ$ | $\frac{1}{2}$        | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ | $\sqrt{3}$           | 
| $45^\circ$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$                  | $1$                  |
| $60^\circ$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$        | $\sqrt{3}$           | $\frac{\sqrt{3}}{3}$ |
| $90^\circ$ | $1$                  | $0$                  | $\times$             | $0$                  |

### Inverzní goniometrické funkce
- K nalezení úhlu díky poměru dvou stran
- $sin^{-1}$, $cos^{-1}$, $tan^{-1}$, $cot^{-1}$

## Euklidovy věty
- ![](https://www.matweb.cz/pictures/euklid1.png)
- **Euklidova věta o výšce**
	- $v_c^2 = c_a \cdot c_b$
		- => $v_c = \sqrt{c_b \cdot c_a}$
- **Euklidova věta o odvěsně**
	- $a^2 = c \cdot c_a$
		- => $a=\sqrt{c \cdot c_a}$
	- $b^2 = c \cdot c_b$
		- => $b=\sqrt{c \cdot c_b}$