import { Component, Input } from '@angular/core';

export interface UserProfile {
  name: string;
  email: string;
  age: number;
  location: string;
  bio: string;
}

@Component({
  selector: 'app-profile-component',
  template: `
    <div class="profile-card">
      <h2>{{ userProfile.name }}</h2>
      <p><strong>Email:</strong> {{ userProfile.email }}</p>
      <p><strong>Age:</strong> {{ userProfile.age }}</p>
      <p><strong>Location:</strong> {{ userProfile.location }}</p>
      <p><strong>Bio:</strong> {{ userProfile.bio }}</p>
    </div>
  `,
  styles: [`
    .profile-card {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 16px;
      max-width: 400px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      font-family: Arial, sans-serif;
    }
    
    .profile-card h2 {
      color: #333;
      margin-top: 0;
    }
    
    .profile-card p {
      margin: 8px 0;
    }
    
    .profile-card strong {
      color: #555;
    }
  `]
})
export class ProfileComponent {
  @Input() userProfile: UserProfile = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    age: 30,
    location: 'New York, USA',
    bio: 'Software developer with a passion for creating amazing web applications.'
  };
}