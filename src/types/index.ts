export interface Question {
  id: number;
  text: string;
  options: string[];
  correctAnswer: number;
  explanation?: string;
}

export interface Assessment {
  id: string;
  title: string;
  description: string;
  role: string;
  questions: Question[];
  passingScore: number; // Percentage
  duration: number; // Minutes
  imageUrl?: string;
}

export interface CandidateDetails {
  name: string;
  age: string;
  gender: string;
  email: string;
  organization: string;
  designation: string;
}

export interface UserResult {
  score: number;
  passed: boolean;
  completedAt: Date;
  certificateId?: string;
  candidateDetails: CandidateDetails;
}
