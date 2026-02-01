import React from 'react';
import { Link } from 'react-router-dom';
import { Clock, CheckCircle, ArrowRight } from 'lucide-react';
import { Assessment } from '../types';

interface AssessmentCardProps {
  assessment: Assessment;
}

export const AssessmentCard: React.FC<AssessmentCardProps> = ({ assessment }) => {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100 hover:shadow-xl transition-shadow flex flex-col h-full">
      {assessment.imageUrl && (
        <img 
          src={assessment.imageUrl} 
          alt={assessment.title} 
          className="w-full h-48 object-cover rounded-lg mb-4"
          onError={(e) => e.currentTarget.style.display = 'none'} 
        />
      )}
      <h3 className="text-xl font-bold text-gray-800 mb-2">{assessment.title}</h3>
      <p className="text-gray-600 mb-4">{assessment.description}</p>
      
      <div className="flex items-center gap-4 text-sm text-gray-500 mb-6">
        <div className="flex items-center gap-1">
          <Clock size={16} />
          <span>{assessment.duration} mins</span>
        </div>
        <div className="flex items-center gap-1">
          <CheckCircle size={16} />
          <span>{assessment.questions.length} Questions</span>
        </div>
      </div>

      <Link
        to={`/assessment/${assessment.id}`}
        className="inline-flex items-center justify-center w-full gap-2 bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
      >
        Start Assessment
        <ArrowRight size={18} />
      </Link>
    </div>
  );
};
