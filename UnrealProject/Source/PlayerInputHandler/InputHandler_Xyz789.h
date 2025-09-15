// InputHandler_Xyz789.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "InputHandler_Xyz789.generated.h"

/**
 * Custom Player Controller class that handles enhanced player input
 */
UCLASS()
class APlayerInputHandler : public APlayerController
{
	GENERATED_BODY()

public:
	// Constructor
	APlayerInputHandler();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called to bind functionality to input
	virtual void SetupInputComponent() override;

private:
	// Input action handlers
	UFUNCTION()
	void MoveForward(float Value);

	UFUNCTION()
	void MoveRight(float Value);

	UFUNCTION()
	void Turn(float Value);

	UFUNCTION()
	void LookUp(float Value);

	UFUNCTION()
	void Jump();

	UFUNCTION()
	void StopJumping();
};