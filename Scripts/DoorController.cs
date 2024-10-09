using System.Collections;
using UnityEngine;

public class DoorController : MonoBehaviour
{
    public Transform door;  // Obiekt drzwi
    public float openSpeed = 3f;  // Pr�dko�� otwierania
    public Vector3 openPositionOffset;  // Jak bardzo drzwi maj� si� otworzy�
    private Vector3 closedPosition;  // Pozycja zamkni�tych drzwi
    private bool isOpen = false;  // Czy drzwi s� otwarte?

    void Start()
    {
        closedPosition = door.position;  // Zapisujemy pozycj� zamkni�tych drzwi
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && !isOpen)  // Sprawdzamy, czy gracz wszed� w trigger i drzwi s� zamkni�te
        {
            StopAllCoroutines();
            StartCoroutine(OpenDoor());  // Rozpoczynamy otwieranie drzwi
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player") && isOpen)  // Sprawdzamy, czy gracz wyszed� z triggera i drzwi s� otwarte
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
        door.position = targetPosition;  // Zapewniamy, �e drzwi ustawi� si� dok�adnie w docelowej pozycji
    }

    IEnumerator CloseDoor()
    {
        isOpen = false;
        while (Vector3.Distance(door.position, closedPosition) > 0.01f)
        {
            door.position = Vector3.Lerp(door.position, closedPosition, Time.deltaTime * openSpeed);
            yield return null;
        }
        door.position = closedPosition;  // Zapewniamy, �e drzwi wr�c� do zamkni�tej pozycji
    }
}
