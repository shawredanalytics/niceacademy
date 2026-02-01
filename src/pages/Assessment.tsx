import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Header } from '../components/Header';
import { infectionControlAssessment } from '../data/questions';
import { ChevronRight, Clock } from 'lucide-react';
import { CandidateDetails } from '../types';

export const AssessmentPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const assessment = infectionControlAssessment; // In a real app, find by ID

  // Shuffle questions on initial load
  const [shuffledQuestions] = useState(() => {
    const shuffled = [...assessment.questions];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  });

  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [showExplanation, setShowExplanation] = useState(false);
  const [isRegistered, setIsRegistered] = useState(false);
  const [timeLeft, setTimeLeft] = useState(assessment.duration * 60); // Duration in seconds

  const [candidateDetails, setCandidateDetails] = useState<CandidateDetails>({
    name: '',
    age: '',
    gender: '',
    email: '',
    organization: '',
    designation: ''
  });

  // Timer logic
  useEffect(() => {
    if (!isRegistered || timeLeft <= 0) return;

    const timer = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmit(true); // Pass true for timedOut
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isRegistered, timeLeft]);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  if (id !== assessment.id) {
    return <div>Assessment not found</div>;
  }

  const handleRegistrationChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setCandidateDetails(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleRegistrationSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (candidateDetails.name && candidateDetails.email) {
      setIsRegistered(true);
    }
  };

  const currentQuestion = shuffledQuestions[currentQuestionIndex];
  const totalQuestions = shuffledQuestions.length;
  const progress = ((currentQuestionIndex + 1) / totalQuestions) * 100;

  const handleOptionSelect = (optionIndex: number) => {
    if (showExplanation) return; // Prevent changing answer after showing explanation
    setAnswers({
      ...answers,
      [currentQuestion.id]: optionIndex,
    });
  };

  const handleNext = () => {
    if (currentQuestionIndex < totalQuestions - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
      setShowExplanation(false);
    } else {
      handleSubmit(false);
    }
  };

  const handleSubmit = (timedOut: boolean = false) => {
    // Calculate score
    let correctCount = 0;
    shuffledQuestions.forEach((q) => {
      if (answers[q.id] === q.correctAnswer) {
        correctCount++;
      }
    });

    const score = (correctCount / totalQuestions) * 100;
    // Fail if timed out, otherwise check score
    const passed = timedOut ? false : score >= assessment.passingScore;
    
    // Save result (in local storage for now)
    const result = {
      score,
      passed,
      completedAt: new Date().toISOString(),
      correctCount,
      totalQuestions,
      candidateDetails,
      timedOut // Add timedOut flag to result if needed for UI
    };
    
    localStorage.setItem('lastResult', JSON.stringify(result));
    navigate('/result');
  };

  if (!isRegistered) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Header />
        <main className="container mx-auto px-4 py-8 max-w-2xl">
          <div className="bg-white rounded-xl shadow-lg p-8">
            <h2 className="text-2xl font-bold text-gray-900 mb-6 text-center">Candidate Registration</h2>
            <p className="text-gray-600 mb-2 text-center">Please provide your details before starting the assessment.</p>
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-8 text-sm text-blue-800">
              <p className="font-semibold mb-1">Assessment Rules:</p>
              <ul className="list-disc list-inside space-y-1">
                <li>Total Duration: 10 Minutes</li>
                <li>Questions: 20 (approx. 30 seconds per question)</li>
                <li>Passing Score: 50%</li>
                <li>If time expires, the assessment will be marked as failed.</li>
              </ul>
            </div>
            
            <form onSubmit={handleRegistrationSubmit} className="space-y-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
                <input
                  type="text"
                  name="name"
                  required
                  value={candidateDetails.name}
                  onChange={handleRegistrationChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Enter your full name"
                />
              </div>

              <div className="grid grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Age</label>
                  <input
                    type="number"
                    name="age"
                    required
                    value={candidateDetails.age}
                    onChange={handleRegistrationChange}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="Age"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Gender</label>
                  <select
                    name="gender"
                    required
                    value={candidateDetails.gender}
                    onChange={handleRegistrationChange}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  >
                    <option value="">Select Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Email ID</label>
                <input
                  type="email"
                  name="email"
                  required
                  value={candidateDetails.email}
                  onChange={handleRegistrationChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="your.email@example.com"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Organization Name</label>
                <input
                  type="text"
                  name="organization"
                  required
                  value={candidateDetails.organization}
                  onChange={handleRegistrationChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Current Organization"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Designation</label>
                <input
                  type="text"
                  name="designation"
                  required
                  value={candidateDetails.designation}
                  onChange={handleRegistrationChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Your Job Title"
                />
              </div>

              <button
                type="submit"
                className="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
              >
                Start Assessment
              </button>
            </form>
          </div>
        </main>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8 max-w-3xl">
        <div className="mb-8">
          <div className="flex justify-between items-center mb-4">
             <div className="flex items-center gap-2 text-gray-700 bg-white px-4 py-2 rounded-lg shadow-sm">
                <Clock size={20} className={timeLeft < 60 ? 'text-red-500' : 'text-blue-600'} />
                <span className={`font-mono text-xl font-bold ${timeLeft < 60 ? 'text-red-500' : 'text-gray-900'}`}>
                  {formatTime(timeLeft)}
                </span>
             </div>
             <span className="text-sm font-medium text-blue-600">
              {Math.round(progress)}% Completed
            </span>
          </div>
          <div className="flex justify-between items-center mb-2">
            <span className="text-sm font-medium text-gray-500">
              Question {currentQuestionIndex + 1} of {totalQuestions}
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2.5">
            <div
              className="bg-blue-600 h-2.5 rounded-full transition-all duration-300"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-8">
          <h2 className="text-xl font-bold text-gray-900 mb-6">
            {currentQuestion.text}
          </h2>

          <div className="space-y-4 mb-8">
            {currentQuestion.options.map((option, index) => (
              <button
                key={index}
                onClick={() => handleOptionSelect(index)}
                className={`w-full text-left p-4 rounded-lg border-2 transition-all ${
                  answers[currentQuestion.id] === index
                    ? 'border-blue-600 bg-blue-50 text-blue-800'
                    : 'border-gray-200 hover:border-blue-300 hover:bg-gray-50'
                }`}
              >
                <div className="flex items-center gap-3">
                  <div
                    className={`w-6 h-6 rounded-full border-2 flex items-center justify-center ${
                      answers[currentQuestion.id] === index
                        ? 'border-blue-600 bg-blue-600'
                        : 'border-gray-300'
                    }`}
                  >
                    {answers[currentQuestion.id] === index && (
                      <div className="w-2 h-2 bg-white rounded-full" />
                    )}
                  </div>
                  <span>{option}</span>
                </div>
              </button>
            ))}
          </div>

          <div className="flex justify-end">
            <button
              onClick={handleNext}
              disabled={answers[currentQuestion.id] === undefined}
              className={`flex items-center gap-2 px-8 py-3 rounded-lg font-semibold transition-colors ${
                answers[currentQuestion.id] !== undefined
                  ? 'bg-blue-600 text-white hover:bg-blue-700'
                  : 'bg-gray-300 text-gray-500 cursor-not-allowed'
              }`}
            >
              {currentQuestionIndex === totalQuestions - 1 ? 'Submit Assessment' : 'Next Question'}
              <ChevronRight size={20} />
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};
