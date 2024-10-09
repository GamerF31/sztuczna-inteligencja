using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class Timer : MonoBehaviour
{
    public TextMeshProUGUI timerText;  // Referencja do tekstu z timerem
    private float timeElapsed = 0f;    // Zmienna do œledzenia czasu

    void Update()
    {
        timeElapsed += Time.deltaTime;  // Zwiêksz czas o czas, który up³yn¹³ od ostatniej klatki
        timerText.text = "Time: " + Mathf.FloorToInt(timeElapsed).ToString();  // Zaktualizuj tekst timera
    }
}
