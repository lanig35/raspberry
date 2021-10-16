#include <Wire.h>

#define DEVICE_ID 0x10

enum {
    CMD_ID = 1,
    CMD_TEMP = 2,
    CMD_LUM = 3
};
byte command = 0;

int nbmsg = 0;

int temp_pin = A0;
#define TEMP_INTERVAL 5000
unsigned long temp_prev_time = 0;
int temp_sensor = 0;
float temperature = 0.0;

int lum_pin = A1;
#define LUM_INTERVAL 10000
unsigned long lum_prev_time = 0;
int lum_sensor = 0;

void sendSensor (int value) {
    byte buffer[2];

    buffer[0] = value >> 8;
    buffer[1] = value & 0xFF;
    Wire.write (buffer, 2);
}

void setup() {
    Serial.begin (9600);
    pinMode (LED_BUILTIN, OUTPUT);

    Wire.begin (DEVICE_ID);
    Wire.onReceive (reception);
    Wire.onRequest (emission);
}

void loop() {
    unsigned long current_time = millis ();

    if ((current_time - temp_prev_time) >= TEMP_INTERVAL) {
        temp_sensor = analogRead (temp_pin);
        float tension = (temp_sensor / 1024.0) * 3.3;
        temperature = (tension -0.5) * 100;
        temp_prev_time = current_time;
        Serial.print ("s:"); Serial.print (temp_sensor);
        Serial.print ("-t: "); Serial.println (temperature);
    }

    if ((current_time - lum_prev_time) >= LUM_INTERVAL) {
        lum_sensor = analogRead (lum_pin);
        lum_prev_time = current_time;
        Serial.print ("l: "); Serial.println (lum_sensor);
    }
}

void reception (int number) {
    command = Wire.read ();
    
    digitalWrite (LED_BUILTIN, !digitalRead (LED_BUILTIN) );
}

void emission () {
    nbmsg++;
    Serial.print ("#msg: "); Serial.println (nbmsg);
    switch (command) {
        case CMD_ID: 	Wire.write (0x31); break;
        case CMD_TEMP:	sendSensor (temp_sensor); break;
        case CMD_LUM:	sendSensor (lum_sensor); break;
    }
}
