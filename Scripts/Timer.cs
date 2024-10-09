using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class Timer : MonoBehaviour
{
    public TextMeshProUGUI timerText;  // Referencja do tekstu z timerem
    private float timeElapsed = 0f;    // Zmienna do �ledzenia czasu

    void Update()
    {
        timeElapsed += Time.deltaTime;  // Zwi�ksz czas o czas, kt�ry up�yn�� od ostatniej klatki
        timerText.text = "Time: " + Mathf.FloorToInt(timeElapsed).ToString();  // Zaktualizuj tekst timera
    }
}
