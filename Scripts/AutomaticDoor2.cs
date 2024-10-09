using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AutomaticDoor2 : MonoBehaviour
{
    public float maximumOpening = 2f;  // Maksymalne otwarcie w jednostkach
    public float maximumClosing = 0f;   // Po³o¿enie zamkniête drzwi
    public float movementSpeed = 5f;      // Prêdkoœæ ruchu
    public GameObject movingDoor;          // Referencja do obiektu drzwi
    private bool playerIsHere;             // Czy gracz jest w obszarze triggera

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
            // Otwieranie drzwi w prawo
            if (movingDoor.transform.localPosition.z > maximumOpening)
            {
                movingDoor.transform.Translate(-movementSpeed * Time.deltaTime, 0f, 0f);
            }
        }
        else
        {
            // Zamykanie drzwi
            if (movingDoor.transform.localPosition.z < maximumClosing)
            {
                movingDoor.transform.Translate(movementSpeed * Time.deltaTime, 0f, 0f);
            }
        }
    }

    private void OnTriggerEnter(Collider col)
    {
        if (col.CompareTag("Player"))
        {
            playerIsHere = true;  // Gracz wszed³ w obszar triggera
        }
    }

    private void OnTriggerExit(Collider col)
    {
        if (col.CompareTag("Player"))
        {
            playerIsHere = false; // Gracz opuœci³ obszar triggera
        }
    }
}
