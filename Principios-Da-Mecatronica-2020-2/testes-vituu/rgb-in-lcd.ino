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
  
  
}

void loop() {
  digitalWrite(RGB_VERM, LIGADO);
  delay(100);
  digitalWrite(RGB_VERM, DESLIGADO);
  delay(50);
  
  digitalWrite(RGB_AZUL, LIGADO);
  delay(100);
  digitalWrite(RGB_AZUL, DESLIGADO);
  delay(50);
  
  digitalWrite(RGB_VERDE, LIGADO);
  delay(100);
  digitalWrite(RGB_VERDE, DESLIGADO);
  delay(50);
  
  lcd.setCursor(0,0);
  lcd.print("Monitor Pot:");
  //Faz a leitura do potenciometro
  int pot = analogRead(5);
  //Limpa a linha no LCD
  lcd.setCursor(0,1);
  lcd.print("                ");
  //Escreve a msg no LCD
  lcd.setCursor(0,1);
  lcd.print(pot);
  //Atualiza a msg a cada 50ms
  delay(500);
}
