const int ENTRADA_1 = 3;
const int ENTRADA_2 = 8;

const int RGB_VERM = 12;
const int RGB_AZUL = 11;
const int RGB_VERDE = 10;

const int LIGADO = HIGH;
const int DESLIGADO = LOW;
const int ENABLE = 2;
const int RS = 13;
const int LCD_D7 = 7;
const int LCD_D6 = 6;
const int LCD_D5 = 5;
const int LCD_D4 = 4;

#include <LiquidCrystal.h>
//Cria uma variável chamada lcd para usar o LCD
LiquidCrystal lcd(RS, ENABLE, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

void setup() {
  //Configurar as entradas
  pinMode(ENTRADA_1, INPUT);
  pinMode(ENTRADA_2, INPUT);
  //Configurar as saídas
  pinMode(RGB_VERM, OUTPUT);
  pinMode(RGB_AZUL, OUTPUT);
  pinMode(RGB_VERDE, OUTPUT);
  
  //Inicializa o LCD
  lcd.begin(16, 2);
  //POsicionar o cursor do LCD
  //lcd.setCursor(0,0); //Coluna x Linha
  //Escrever uma msg no LCD
  //lcd.print("Monitor Pot:");
  digitalWrite(ENTRADA_1, LIGADO);
  
}

void loop() {
  
  digitalWrite(RGB_VERM, LIGADO);
  delay(3000);
  digitalWrite(RGB_VERM, DESLIGADO);
  delay(2000);
  
  digitalWrite(RGB_AZUL, LIGADO);
  delay(5000);
  digitalWrite(RGB_AZUL, DESLIGADO);
  delay(3500);
  
  digitalWrite(RGB_VERDE, LIGADO);
  delay(2000);
  digitalWrite(RGB_VERDE, DESLIGADO);
  delay(1300);
  
  lcd.setCursor(0,0);
  lcd.print("Cor acesa:");
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,1);
  
  //if a partir daqui
  if((digitalRead(RGB_VERDE) == DESLIGADO)&&(digitalRead(RGB_AZUL) == DESLIGADO)&&(digitalRead(RGB_VERM) == LIGADO)){
    lcd.print("VERMELHO");
  } else if((digitalRead(RGB_VERDE) == DESLIGADO)&&(digitalRead(RGB_AZUL) == LIGADO)&&(digitalRead(RGB_VERM) == DESLIGADO)){
    lcd.print("AZUL");
  } else if((digitalRead(RGB_VERDE) == LIGADO)&&(digitalRead(RGB_AZUL) == DESLIGADO)&&(digitalRead(RGB_VERM) == DESLIGADO)){
    lcd.print("VERDE");
  } else if((digitalRead(RGB_VERDE) == LIGADO)&&(digitalRead(RGB_AZUL) == LIGADO)&&(digitalRead(RGB_VERM) == LIGADO)){
    lcd.print("RGB INTEIRO");
  } else {
    lcd.print("INDEFINIDO");
  }
  delay(200);
}


//falhou
