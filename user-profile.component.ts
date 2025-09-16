import { Component, Input } from '@angular/core';

export interface UserProfile {
  name: string;
  email: string;
  avatarUrl?: string;
  bio?: string;
  joinDate?: Date;
}

@Component({
  selector: 'app-user-profile',
  template: `
    <div class="user-profile">
      <div class="profile-header">
        <img *ngIf="profile.avatarUrl" [src]="profile.avatarUrl" alt="{{profile.name}}" class="avatar">
        <div class="basic-info">
          <h2>{{ profile.name }}</h2>
          <p>{{ profile.email }}</p>
        </div>
      </div>
      <div class="profile-details" *ngIf="profile.bio || profile.joinDate">
        <p *ngIf="profile.bio">{{ profile.bio }}</p>
        <p *ngIf="profile.joinDate">Member since: {{ profile.joinDate | date }}</p>
      </div>
    </div>
  `,
  styles: [`
    .user-profile {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 16px;
      max-width: 400px;
      font-family: Arial, sans-serif;
    }
    .profile-header {
      display: flex;
      align-items: center;
      margin-bottom: 16px;
    }
    .avatar {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      margin-right: 16px;
    }
    .basic-info h2 {
      margin: 0 0 8px 0;
      color: #333;
    }
    .basic-info p {
      margin: 0;
      color: #666;
    }
    .profile-details p {
      margin: 8px 0;
      color: #555;
    }
  `]
})
export class UserProfileComponent {
  @Input() profile: UserProfile = {
    name: '',
    email: ''
  };
}