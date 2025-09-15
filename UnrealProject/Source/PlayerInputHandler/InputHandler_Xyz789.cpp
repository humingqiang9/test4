// InputHandler_Xyz789.cpp
#include "InputHandler_Xyz789.h"
#include "GameFramework/Character.h"
#include "GameFramework/Controller.h"
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h"
#include "InputAction.h"
#include "Engine/World.h"

// Constructor
APlayerInputHandler::APlayerInputHandler()
{
	// Set this controller to call Tick() every frame
	PrimaryActorTick.bCanEverTick = true;
}

// Called when the game starts or when spawned
void APlayerInputHandler::BeginPlay()
{
	Super::BeginPlay();

	// Get the player controller
	APlayerController* PlayerController = Cast<APlayerController>(GetController());
	if (PlayerController)
	{
		// Add input mapping context
		if (UEnhancedInputLocalPlayerSubsystem* Subsystem = ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(PlayerController->GetLocalPlayer()))
		{
			//Subsystem->AddMappingContext(DefaultMappingContext, 0);
		}
	}
}

// Called to bind functionality to input
void APlayerInputHandler::SetupInputComponent()
{
	Super::SetupInputComponent();

	// Cast to enhanced input component
	if (UEnhancedInputComponent* EnhancedInputComponent = CastChecked<UEnhancedInputComponent>(InputComponent))
	{
		// Bind input actions
		// EnhancedInputComponent->BindAction(MoveAction, ETriggerEvent::Triggered, this, &APlayerInputHandler::Move);
		// EnhancedInputComponent->BindAction(JumpAction, ETriggerEvent::Started, this, &APlayerInputHandler::Jump);
		// EnhancedInputComponent->BindAction(JumpAction, ETriggerEvent::Completed, this, &APlayerInputHandler::StopJumping);
	}
}

// Input action handlers
void APlayerInputHandler::MoveForward(float Value)
{
	if ((GetPawn() != nullptr) && (Value != 0.0f))
	{
		// Find out which way is forward
		const FRotator Rotation = GetControlRotation();
		const FRotator YawRotation(0, Rotation.Yaw, 0);

		// Get forward vector
		const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
		GetPawn()->AddMovementInput(Direction, Value);
	}
}

void APlayerInputHandler::MoveRight(float Value)
{
	if ((GetPawn() != nullptr) && (Value != 0.0f))
	{
		// Find out which way is right
		const FRotator Rotation = GetControlRotation();
		const FRotator YawRotation(0, Rotation.Yaw, 0);

		// Get right vector
		const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y);
		GetPawn()->AddMovementInput(Direction, Value);
	}
}

void APlayerInputHandler::Turn(float Value)
{
	AddYawInput(Value);
}

void APlayerInputHandler::LookUp(float Value)
{
	AddPitchInput(Value);
}

void APlayerInputHandler::Jump()
{
	if (GetPawn() != nullptr)
	{
		GetPawn()->Jump();
	}
}

void APlayerInputHandler::StopJumping()
{
	if (GetPawn() != nullptr)
	{
		GetPawn()->StopJumping();
	}
}