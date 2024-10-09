using System.Collections;
using UnityEngine;
using TMPro; // U¿ywamy TextMeshPro

public class WelcomeMessage : MonoBehaviour
{
    public TextMeshProUGUI welcomeText;  // Referencja do tekstu
    public float displayTime = 3f;       // Czas wyœwietlania tekstu w sekundach

    void Start()
    {
        welcomeText.gameObject.SetActive(true);  // W³¹cz tekst na pocz¹tku
        StartCoroutine(HideTextAfterDelay());    // Ukryj tekst po okreœlonym czasie
    }

    IEnumerator HideTextAfterDelay()
    {
        yield return new WaitForSeconds(displayTime);  // Czekaj kilka sekund
        welcomeText.gameObject.SetActive(false);       // Ukryj tekst
    }
}
