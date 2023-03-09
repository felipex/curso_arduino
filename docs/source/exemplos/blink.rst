Blink - Saída Digital
=====================================

Pisca LED 
-----------------


Hardware necessário
-------------------

* 1 Placa de Arduino
* 1 LED
* Resistor 330 Ohms
* Jumpers
* Protoboard

Diagrama
--------

.. figure:: ../img/exemplo01-1.png


Sketch
-------


literalinclude: /home/felipe/repositorios/ESp-MicroPython/code/Blink_LED.py

.. code-block:: c++

	void setup() {
	  // initialize digital pin LED_BUILTIN as an output.
	  pinMode(LED_BUILTIN, OUTPUT);
	}

	// the loop function runs over and over again forever
	void loop() {
	  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
	  delay(1000);                      // wait for a second
	  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
	  delay(1000);                      // wait for a second
	}





