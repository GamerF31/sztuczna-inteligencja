using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CharacterController))]
public class PlayerMovement : MonoBehaviour
{
    public Camera playerCamera;
    public float walkSpeed = 50f;
    public float runSpeed = 82f;
    public float jumpPower = 40f;  // Upewnij siê, ¿e ta wartoœæ jest u¿ywana w kodzie
    public float gravity = 80f;
    public float lookSpeed = 13f;
    public float lookXLimit = 45f;
    public float defaultHeight = 2f;
    public float crouchHeight = 1f;
    public float crouchSpeed = 40f; // Ustaw wiêksz¹ wartoœæ, aby zwiêkszyæ prêdkoœæ kucania

    private Vector3 moveDirection = Vector3.zero;
    private float rotationX = 0;
    private CharacterController characterController;

    private bool canMove = true;

    void Start()
    {
        characterController = GetComponent<CharacterController>();
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;

        // Ustawienia domyœlne
        jumpPower = 40f; // Zmieñ tê wartoœæ wed³ug potrzeb
        crouchSpeed = 40f; // Zmieñ tê wartoœæ wed³ug potrzeb
        gravity = 80f;
    }

    void Update()
    {
        Vector3 forward = transform.TransformDirection(Vector3.forward);
        Vector3 right = transform.TransformDirection(Vector3.right);

        bool isRunning = Input.GetKey(KeyCode.LeftShift);
        float curSpeedX = canMove ? (isRunning ? runSpeed : walkSpeed) * Input.GetAxis("Vertical") : 0;
        float curSpeedY = canMove ? (isRunning ? runSpeed : walkSpeed) * Input.GetAxis("Horizontal") : 0;
        float movementDirectionY = moveDirection.y;
        moveDirection = (forward * curSpeedX) + (right * curSpeedY);

        // Dodanie skoku
        if (Input.GetButton("Jump") && canMove && characterController.isGrounded)
        {
            moveDirection.y = jumpPower;
        }
        else
        {
            moveDirection.y = movementDirectionY;
        }

        if (characterController.isGrounded)
        {
            moveDirection.y = -0.5f;  // Lekko utrzymujemy gracza na ziemi
            if (Input.GetButton("Jump") && canMove)
            {
                moveDirection.y = jumpPower;  // U¿ywamy jumpPower w odpowiednim miejscu
            }
        }
        else
        {
            moveDirection.y -= gravity * Time.deltaTime;  // Wprowadzenie naturalnej grawitacji
        }

        // Kucanie
        if (Input.GetKey(KeyCode.R) && canMove)
        {
            characterController.height = Mathf.Lerp(characterController.height, crouchHeight, Time.deltaTime * 10f); // Zwiêkszenie prêdkoœci przejœcia do kucania
            walkSpeed = crouchSpeed;
            runSpeed = crouchSpeed;
        }
        else
        {
            characterController.height = Mathf.Lerp(characterController.height, defaultHeight, Time.deltaTime * 10f);
            walkSpeed = 50f;  // Utrzymanie standardowej prêdkoœci chodzenia
            runSpeed = 82f;
        }

        characterController.Move(moveDirection * Time.deltaTime);

        if (canMove)
        {
            rotationX += -Input.GetAxis("Mouse Y") * lookSpeed;
            rotationX = Mathf.Clamp(rotationX, -lookXLimit, lookXLimit);
            playerCamera.transform.localRotation = Quaternion.Euler(rotationX, 0, 0);
            transform.rotation *= Quaternion.Euler(0, Input.GetAxis("Mouse X") * lookSpeed, 0);
        }
    }
}
