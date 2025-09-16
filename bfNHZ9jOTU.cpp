// bfNHZ9jOTU.cpp
// Player input handler class for Unreal Engine

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/Character.h"
#include "GameFramework/PlayerInput.h"
#include "InputCoreTypes.h"
#include "Engine/World.h"

// Player input handler class
class PlayerInputHandler
{
public:
    PlayerInputHandler();
    ~PlayerInputHandler();

    // Setup input bindings
    void SetupInput(class APlayerController* PlayerController);

    // Input action handlers
    void OnJumpPressed();
    void OnJumpReleased();
    void OnFirePressed();
    void OnFireReleased();
    
    // Input axis handlers
    void OnMoveForward(float Value);
    void OnMoveRight(float Value);
    void OnTurn(float Value);
    void OnLookUp(float Value);

private:
    class ACharacter* ControlledCharacter;
};

// Constructor
PlayerInputHandler::PlayerInputHandler()
{
    ControlledCharacter = nullptr;
}

// Destructor
PlayerInputHandler::~PlayerInputHandler()
{
}

// Setup input bindings
void PlayerInputHandler::SetupInput(class APlayerController* PlayerController)
{
    if (PlayerController)
    {
        // Get the character that the player controller is possessing
        ControlledCharacter = PlayerController->GetCharacter();
        
        // Bind action mappings
        PlayerController->InputComponent->BindAction("Jump", IE_Pressed, this, &PlayerInputHandler::OnJumpPressed);
        PlayerController->InputComponent->BindAction("Jump", IE_Released, this, &PlayerInputHandler::OnJumpReleased);
        PlayerController->InputComponent->BindAction("Fire", IE_Pressed, this, &PlayerInputHandler::OnFirePressed);
        PlayerController->InputComponent->BindAction("Fire", IE_Released, this, &PlayerInputHandler::OnFireReleased);
        
        // Bind axis mappings
        PlayerController->InputComponent->BindAxis("MoveForward", this, &PlayerInputHandler::OnMoveForward);
        PlayerController->InputComponent->BindAxis("MoveRight", this, &PlayerInputHandler::OnMoveRight);
        PlayerController->InputComponent->BindAxis("Turn", this, &PlayerInputHandler::OnTurn);
        PlayerController->InputComponent->BindAxis("LookUp", this, &PlayerInputHandler::OnLookUp);
    }
}

// Jump action handlers
void PlayerInputHandler::OnJumpPressed()
{
    if (ControlledCharacter)
    {
        ControlledCharacter->Jump();
    }
}

void PlayerInputHandler::OnJumpReleased()
{
    if (ControlledCharacter)
    {
        ControlledCharacter->StopJumping();
    }
}

// Fire action handlers
void PlayerInputHandler::OnFirePressed()
{
    // Implement fire logic here
    UE_LOG(LogTemp, Warning, TEXT("Fire pressed"));
}

void PlayerInputHandler::OnFireReleased()
{
    // Implement fire release logic here
    UE_LOG(LogTemp, Warning, TEXT("Fire released"));
}

// Movement axis handlers
void PlayerInputHandler::OnMoveForward(float Value)
{
    if (ControlledCharacter && Value != 0.0f)
    {
        // Get forward direction
        FRotator Rotation = ControlledCharacter->GetControlRotation();
        FRotator YawRotation(0, Rotation.Yaw, 0);
        
        // Move in the direction of the character's forward vector
        FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
        ControlledCharacter->AddMovementInput(Direction, Value);
    }
}

void PlayerInputHandler::OnMoveRight(float Value)
{
    if (ControlledCharacter && Value != 0.0f)
    {
        // Get right direction
        FRotator Rotation = ControlledCharacter->GetControlRotation();
        FRotator YawRotation(0, Rotation.Yaw, 0);
        
        // Move in the direction of the character's right vector
        FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y);
        ControlledCharacter->AddMovementInput(Direction, Value);
    }
}

// Look axis handlers
void PlayerInputHandler::OnTurn(float Value)
{
    if (ControlledCharacter && Value != 0.0f)
    {
        ControlledCharacter->AddControllerYawInput(Value);
    }
}

void PlayerInputHandler::OnLookUp(float Value)
{
    if (ControlledCharacter && Value != 0.0f)
    {
        ControlledCharacter->AddControllerPitchInput(Value);
    }
}