using UnityEngine;

public class MovableBlock : MonoBehaviour
{
    private bool isMoving = false;
    private Vector3 targetPosition;

    void Update()
    {
        if (isMoving)
        {
            transform.position = Vector3.MoveTowards(transform.position, targetPosition, Time.deltaTime * 3f);
            if (transform.position == targetPosition)
            {
                isMoving = false;
            }
        }
    }

    void OnMouseDown()
    {
        targetPosition = transform.position + Vector3.right; // Przesuniêcie w prawo
        isMoving = true;
    }
}
