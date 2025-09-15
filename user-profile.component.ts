import { Component, Input } from '@angular/core';

export interface UserProfile {
  id: number;
  name: string;
  email: string;
  avatarUrl?: string;
  bio?: string;
  joinDate?: string;
}

@Component({
  selector: 'app-user-profile',
  template: `
    <div class="user-profile" *ngIf="user">
      <div class="profile-header">
        <img [src]="user.avatarUrl || 'assets/default-avatar.png'" 
             [alt]="user.name"
             class="profile-avatar">
        <div class="profile-basic-info">
          <h2>{{ user.name }}</h2>
          <p class="user-email">{{ user.email }}</p>
        </div>
      </div>
      
      <div class="profile-details" *ngIf="user.bio || user.joinDate">
        <p *ngIf="user.bio" class="user-bio">{{ user.bio }}</p>
        <p *ngIf="user.joinDate" class="join-date">
          Member since: {{ user.joinDate | date:'mediumDate' }}
        </p>
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
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      font-family: Arial, sans-serif;
    }
    
    .profile-header {
      display: flex;
      align-items: center;
      margin-bottom: 20px;
    }
    
    .profile-avatar {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      object-fit: cover;
      margin-right: 20px;
    }
    
    .profile-basic-info h2 {
      margin: 0 0 5px 0;
      color: #333;
    }
    
    .user-email {
      margin: 0;
      color: #666;
      font-size: 14px;
    }
    
    .profile-details {
      border-top: 1px solid #eee;
      padding-top: 15px;
    }
    
    .user-bio {
      font-style: italic;
      color: #555;
      line-height: 1.4;
    }
    
    .join-date {
      font-size: 12px;
      color: #888;
      margin-top: 10px;
    }
  `]
})
export class UserProfileComponent {
  @Input() user: UserProfile | null = null;
}