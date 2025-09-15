# Project Overview

This repository contains a collection of utilities including an Angular component for displaying user profiles and a PowerShell script for date/time operations.

## Contents

1. **Profile Component** (`profile-component-zkOShRMoeS.ts`): An Angular component that displays user profile information in a card format.
2. **PowerShell Script** (`powershell_scripts/SklgaYS5KR.ps1`): A simple script that outputs the current date and time.

## Installation

### Prerequisites

- For the Angular component:
  - Node.js (version 12 or higher)
  - Angular CLI
  
- For the PowerShell script:
  - Windows OS with PowerShell installed

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. For Angular development (if expanding on the profile component):
   ```bash
   npm install -g @angular/cli
   npm install
   ```

## Usage

### Profile Component

To use the profile component in your Angular application:

1. Copy the `ProfileComponent` class and `UserProfile` interface to your Angular project.
2. Import the component in your module:
   ```typescript
   import { ProfileComponent } from './path/to/profile-component';
   
   @NgModule({
     declarations: [
       ProfileComponent,
       // other components
     ],
     // ...
   })
   export class AppModule { }
   ```
3. Use the component in your templates:
   ```html
   <app-profile-component></app-profile-component>
   ```
4. Optionally, pass a custom user profile object:
   ```html
   <app-profile-component [userProfile]="customUserProfile"></app-profile-component>
   ```

### PowerShell Script

To run the PowerShell script:

1. Navigate to the script directory:
   ```cmd
   cd powershell_scripts
   ```
2. Execute the script:
   ```powershell
   .\SklgaYS5KR.ps1
   ```

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.