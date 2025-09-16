// user-profile.component.ts
import { Component, Input } from '@angular/core';

export interface UserProfile {
  id: number;
  name: string;
  email: string;
  avatarUrl?: string;
  bio?: string;
  joinDate: Date;
}

@Component({
  selector: 'app-user-profile',
  template: `
    <div class="user-profile">
      <div class="profile-header">
        <img *ngIf="profile.avatarUrl; else defaultAvatar" 
             [src]="profile.avatarUrl" 
             alt="{{profile.name}}'s avatar" 
             class="avatar">
        <ng-template #defaultAvatar>
          <div class="default-avatar">{{profile.name.charAt(0)}}</div>
        </ng-template>
        <h2>{{ profile.name }}</h2>
      </div>
      
      <div class="profile-details">
        <p><strong>Email:</strong> {{ profile.email }}</p>
        <p *ngIf="profile.bio"><strong>Bio:</strong> {{ profile.bio }}</p>
        <p><strong>Member since:</strong> {{ profile.joinDate | date:'longDate' }}</p>
      </div>
    </div>
  `,
  styles: [`
    .user-profile {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 20px;
      max-width: 400px;
      font-family: Arial, sans-serif;
    }
    
    .profile-header {
      text-align: center;
      margin-bottom: 20px;
    }
    
    .avatar {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      object-fit: cover;
    }
    
    .default-avatar {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background-color: #007bff;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 40px;
      font-weight: bold;
      margin: 0 auto;
    }
    
    .profile-details p {
      margin: 10px 0;
    }
  `]
})
export class UserProfileComponent {
  @Input() profile!: UserProfile;
}