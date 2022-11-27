#include <Wire.h>

#define DEVICE_ID 0x10

enum {
    CMD_ID = 1,
    CMD_TEMP = 2,
    CMD_LUM = 3,
    CMD_BME = 4
};
byte command = 0;

int nbmsg = 0;

int temp_pin = A0;
#define TEMP_INTERVAL 5000
#define WINDOW_SIZE 5
unsigned long temp_prev_time = 0;
int temp_capteur [WINDOW_SIZE];
int index = 0;
int temp_moyenne = 0;

int lum_pin = A1;
#define LUM_INTERVAL 10000
unsigned long lum_prev_time = 0;
int lum_capteur = 0;

void sendSensor (int valeur) {
    byte buffer[2];

    buffer[0] = valeur >> 8;
    buffer[1] = valeur & 0xFF;
    Wire.write (buffer, 2);
}

void setup() {
    Serial.begin (9600);
    pinMode (LED_BUILTIN, OUTPUT);

    Wire.begin (DEVICE_ID);
    Wire.onReceive (reception);
    Wire.onRequest (emission);

    temp_moyenne = analogRead (temp_pin);
    for (int i=0; i<WINDOW_SIZE; i++) {
        temp_capteur[i] = temp_moyenne;
    }
}

void loop() {
    unsigned long current_time = millis ();

    if ((current_time - temp_prev_time) >= TEMP_INTERVAL) {
        int somme = 0;
        float temperature = 0.0;

        int capteur = analogRead (temp_pin);

        temp_capteur[index] = capteur;
        index = (index + 1) % WINDOW_SIZE;
        for (int i=0; i<WINDOW_SIZE; i++) {
           somme = somme + temp_capteur[i];
        }
        temp_moyenne = somme / WINDOW_SIZE;
 
        float tension = (temp_moyenne / 1024.0) * 3.3;
        temperature = (tension -0.5) * 100;

        temp_prev_time = current_time;

        Serial.print ("a:"); Serial.print (temp_moyenne);
        Serial.print ("-s:"); Serial.print (capteur);
        Serial.print ("-t:"); Serial.println (temperature);
    }

    if ((current_time - lum_prev_time) >= LUM_INTERVAL) {
        lum_capteur = analogRead (lum_pin);
        lum_prev_time = current_time;
        Serial.print ("l: "); Serial.println (lum_capteur);
    }
}

void reception (int number) {
    digitalWrite (LED_BUILTIN, !digitalRead (LED_BUILTIN) );
    
    Serial.print ("reçu: "); Serial.print (number);

    command = Wire.read ();

    if ((command == CMD_BME) && (number > 1)) {
       char message[8];
       int i = 0;

       Serial.print (" - ");
       while (Wire.available()) {
           message[i] = Wire.read();
           Serial.print (message[i], HEX);
           i++;
      }
      message[i] = '\0';
      float bme = (float)atof(message);
      Serial.print (" : "); Serial.print (bme);
   }
   Serial.println ("");    
}

void emission () {
    nbmsg++;
    Serial.print ("#msg: "); Serial.println (nbmsg);

    switch (command) {
        case CMD_ID: 	Wire.write (0x31); break;
        case CMD_TEMP:	sendSensor (temp_moyenne); break;
        case CMD_LUM:	sendSensor (lum_capteur); break;
    }
}
