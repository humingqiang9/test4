import { Component, Input } from '@angular/core';

export interface UserProfile {
  id: number;
  name: string;
  email: string;
  avatarUrl?: string;
  bio?: string;
  location?: string;
  joinDate?: Date;
}

@Component({
  selector: 'app-user-profile',
  template: `
    <div class="user-profile">
      <div class="profile-header">
        <img *ngIf="profile.avatarUrl; else defaultAvatar" 
             [src]="profile.avatarUrl" 
             [alt]="profile.name"
             class="avatar">
        <ng-template #defaultAvatar>
          <div class="default-avatar">{{ profile.name.charAt(0) }}</div>
        </ng-template>
        <h2>{{ profile.name }}</h2>
      </div>
      
      <div class="profile-details">
        <div class="detail-item">
          <strong>Email:</strong>
          <span>{{ profile.email }}</span>
        </div>
        
        <div class="detail-item" *ngIf="profile.bio">
          <strong>Bio:</strong>
          <span>{{ profile.bio }}</span>
        </div>
        
        <div class="detail-item" *ngIf="profile.location">
          <strong>Location:</strong>
          <span>{{ profile.location }}</span>
        </div>
        
        <div class="detail-item" *ngIf="profile.joinDate">
          <strong>Member since:</strong>
          <span>{{ profile.joinDate | date:'mediumDate' }}</span>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .user-profile {
      max-width: 500px;
      margin: 20px auto;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
      font-family: Arial, sans-serif;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
      margin-bottom: 10px;
    }
    
    .default-avatar {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background-color: #3f51b5;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 40px;
      font-weight: bold;
      margin: 0 auto 10px;
    }
    
    h2 {
      margin: 0;
      color: #333;
    }
    
    .profile-details {
      text-align: left;
    }
    
    .detail-item {
      display: flex;
      margin-bottom: 10px;
    }
    
    .detail-item strong {
      width: 120px;
      color: #555;
    }
    
    .detail-item span {
      flex: 1;
      color: #333;
    }
  `]
})
export class UserProfileComponent {
  @Input() profile: UserProfile = {
    id: 0,
    name: '',
    email: ''
  };
}