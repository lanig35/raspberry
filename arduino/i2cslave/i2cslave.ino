#include <Wire.h>

#define DEVICE_ID 0x10

char message [8];
int nbmsg = 0;

void setup() {
    Serial.begin (9600);
    pinMode (LED_BUILTIN, OUTPUT);

    Wire.begin (DEVICE_ID);
    Wire.onReceive (reception);
    Wire.onRequest (emission);
}

void loop() {
}

void reception (int number) {
    int indice = 0;

    while (Wire.available()) {
        message [indice] = Wire.read ();
        indice++;
    }
    Serial.print ("emsg: "); Serial.println (message);
    if (digitalRead (LED_BUILTIN) == HIGH) {
        digitalWrite (LED_BUILTIN, LOW);
    } else {
        digitalWrite (LED_BUILTIN, HIGH);
    }
}

void emission () {
    nbmsg++;
    Serial.print ("reçu: "); Serial.println (nbmsg);
    Wire.write ("AB");
}
