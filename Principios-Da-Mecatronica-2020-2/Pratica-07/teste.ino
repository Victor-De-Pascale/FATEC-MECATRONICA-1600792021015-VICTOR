const int LED_VERDE = 5;
const int LED_AZUL = 3;
const int LED_VERMELHO = 1;
const int LED_BRANCO = 2;
const int LED_AMARELO = 4;
const int BOTAO_1 = 8;
const int BOTAO_2 = 9;
const int LIG = HIGH;
const int DESL = LOW;

void setup()
{
  //pinMode(13, OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);//PINO DE SAIDA
  pinMode(LED_AZUL, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_BRANCO, OUTPUT);
  pinMode(LED_AMARELO, OUTPUT);
  pinMode(BOTAO_1, INPUT);//PINO DE ENTRADA
  pinMode(BOTAO_2, INPUT);
}

void loop()
{
  
  //TESTE
  digitalWrite(LED_VERDE, LIG);
  if (digitalRead(LED_VERDE) == LIG){
    digitalWrite(LED_VERDE, DESL);
    digitalWrite(LED_VERMELHO, LIG);
  	delay(100);
  	digitalWrite(LED_VERMELHO, DESL);
  	digitalWrite(LED_BRANCO, LIG);
  	delay(100);
  	digitalWrite(LED_BRANCO, DESL);
  	digitalWrite(LED_AZUL, LIG);
  	delay(100);
  	digitalWrite(LED_AZUL, DESL);
  	digitalWrite(LED_AMARELO, LIG);
  	delay(100);
  	digitalWrite(LED_AMARELO, DESL);
  	digitalWrite(LED_VERDE, LIG);
  	delay(100);
  }
}
