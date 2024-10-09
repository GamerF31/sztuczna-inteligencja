using System.Collections;
using UnityEngine;

public class DoorController : MonoBehaviour
{
    public Transform door;  // Obiekt drzwi
    public float openSpeed = 3f;  // Prêdkoœæ otwierania
    public Vector3 openPositionOffset;  // Jak bardzo drzwi maj¹ siê otworzyæ
    private Vector3 closedPosition;  // Pozycja zamkniêtych drzwi
    private bool isOpen = false;  // Czy drzwi s¹ otwarte?

    void Start()
    {
        closedPosition = door.position;  // Zapisujemy pozycjê zamkniêtych drzwi
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && !isOpen)  // Sprawdzamy, czy gracz wszed³ w trigger i drzwi s¹ zamkniête
        {
            StopAllCoroutines();
            StartCoroutine(OpenDoor());  // Rozpoczynamy otwieranie drzwi
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player") && isOpen)  // Sprawdzamy, czy gracz wyszed³ z triggera i drzwi s¹ otwarte
        {
            StopAllCoroutines();
            StartCoroutine(CloseDoor());  // Rozpoczynamy zamykanie drzwi
        }
    }

    IEnumerator OpenDoor()
    {
        isOpen = true;
        Vector3 targetPosition = closedPosition + openPositionOffset;
        while (Vector3.Distance(door.position, targetPosition) > 0.01f)
        {
            door.position = Vector3.Lerp(door.position, targetPosition, Time.deltaTime * openSpeed);
            yield return null;
        }
        door.position = targetPosition;  // Zapewniamy, ¿e drzwi ustawi¹ siê dok³adnie w docelowej pozycji
    }

    IEnumerator CloseDoor()
    {
        isOpen = false;
        while (Vector3.Distance(door.position, closedPosition) > 0.01f)
        {
            door.position = Vector3.Lerp(door.position, closedPosition, Time.deltaTime * openSpeed);
            yield return null;
        }
        door.position = closedPosition;  // Zapewniamy, ¿e drzwi wróc¹ do zamkniêtej pozycji
    }
}
