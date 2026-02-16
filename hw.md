# Python Exercise — Inheritance, Override, and Abstract Classes (ABC)

## 🎯 Goal

Practice:

* Abstract classes (`ABC`)
* Interfaces (abstract methods)
* Inheritance
* Method overriding
* Multiple inheritance

Keep the solution simple and clean.

## 📋 Exercise Description

Create a small system for **vehicles and charging**.

### 1️⃣ Create interface `Chargeable`

* Use `ABC`
* Abstract method:

```python
charge()
```

### 2️⃣ Create interface `Drivable`

* Use `ABC`
* Abstract method:

```python
drive()
```

### 3️⃣ Create abstract class `Vehicle`

Fields:

* `model`

Methods:

* `__init__`
* `__str__`
* abstract method:

```python
move()
```

### 4️⃣ Create class `ElectricCar`

Inheritance:

* inherits from `Vehicle`
* implements `Chargeable`
* implements `Drivable`

Fields:

* `battery_level`

Methods:

* `__init__`
* `__str__`
* override `move()`
* implement `charge()`
* implement `drive()`

Behavior example:

* `move()` → prints that the car moves silently
* `drive()` → prints driving message
* `charge()` → prints charging message

### 5️⃣ Create class `ElectricScooter`

Inheritance:

* inherits from `Vehicle`
* implements `Chargeable`

Fields:

* `max_speed`

Methods:

* `__init__`
* `__str__`
* override `move()`
* implement `charge()`

### 6️⃣ Create objects and test

* Create at least:

  * one `ElectricCar`
  * one `ElectricScooter`

Call:

* `move()`
* `charge()`
* `drive()` (only where relevant)
* `print(object)`

## 🌳 Expected Inheritance Tree

```
Vehicle (abstract)
│
├── ElectricCar --------┐
│                       ├── Chargeable (interface)
│                       └── Drivable (interface)
│
└── ElectricScooter ----┘
                        └── Chargeable (interface)
```

## 🧠 Tips

* Use `from abc import ABC, abstractmethod`
* Use `@abstractmethod`
* Use `@override` from `typing_extensions` (optional)
* Keep methods short and clear

---

Good luck 🚀

Submit email: **[pythonai200425+oopint@gmail.com](mailto:pythonai200425+oopint@gmail.com)**
