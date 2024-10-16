using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AutomaticDoor : MonoBehaviour
{
    public float maximumOpening = 2f;  // Maksymalne otwarcie w jednostkach
    public float maximumClosing = 0f;   // Po�o�enie zamkni�te drzwi
    public float movementSpeed = 5f;     // Pr�dko�� ruchu
    public GameObject movingDoor;        // Referencja do obiektu drzwi
    private bool playerIsHere;           // Czy gracz jest w obszarze triggera

    // Start is called before the first frame update
    void Start()
    {
        playerIsHere = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (playerIsHere)
        {
            // Otwieranie drzwi
            if (movingDoor.transform.localPosition.z < maximumOpening)
            {
                movingDoor.transform.Translate(0f, 0f, movementSpeed * Time.deltaTime);
            }
        }
        else
        {
            // Zamykanie drzwi
            if (movingDoor.transform.localPosition.z > maximumClosing)
            {
                movingDoor.transform.Translate(0f, 0f, -movementSpeed * Time.deltaTime);
            }
        }
    }

    private void OnTriggerEnter(Collider col)
    {
        if (col.CompareTag("Player"))
        {
            playerIsHere = true;  // Gracz wszed� w obszar triggera
        }
    }

    private void OnTriggerExit(Collider col)
    {
        if (col.CompareTag("Player"))
        {
            playerIsHere = false; // Gracz opu�ci� obszar triggera
        }
    }
}