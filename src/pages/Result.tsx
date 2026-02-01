import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Header } from '../components/Header';
import { CheckCircle, XCircle, RefreshCw, Download, Home as HomeIcon } from 'lucide-react';
import { infectionControlAssessment } from '../data/questions';

export const ResultPage: React.FC = () => {
  const navigate = useNavigate();
  const resultString = localStorage.getItem('lastResult');
  
  if (!resultString) {
    return <div className="text-center py-12">No results found. <Link to="/" className="text-blue-600">Go Home</Link></div>;
  }

  const result = JSON.parse(resultString);
  const { score, passed, correctCount, totalQuestions, completedAt, timedOut, candidateDetails } = result;

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="min-h-screen bg-gray-50 print:bg-white">
      <div className="print:hidden">
        <Header />
      </div>
      
      <main className="container mx-auto px-4 py-12 max-w-4xl">
        <div className="bg-white rounded-xl shadow-lg p-8 text-center print:shadow-none print:p-0">
          <div className="mb-6 flex justify-center print:hidden">
            {passed ? (
              <CheckCircle className="text-green-500 w-20 h-20" />
            ) : (
              <XCircle className="text-red-500 w-20 h-20" />
            )}
          </div>

          <h1 className="text-3xl font-bold mb-2 text-gray-900">
            {passed ? 'Congratulations!' : timedOut ? 'Time Limit Exceeded' : 'Assessment Not Passed'}
          </h1>
          
          <p className="text-xl text-gray-600 mb-8">
            {timedOut ? (
              <span className="text-red-600 font-medium block mb-2">
                You failed to complete the assessment within the 10-minute limit.
              </span>
            ) : null}
            You scored {Math.round(score)}% ({correctCount}/{totalQuestions} correct)
          </p>

          <div className="flex justify-center gap-4 mb-12 print:hidden">
            <Link
              to="/"
              className="flex items-center gap-2 px-6 py-3 border border-gray-300 rounded-lg font-semibold hover:bg-gray-50 transition-colors"
            >
              <HomeIcon size={20} />
              Back to Home
            </Link>
            
            {!passed && (
              <button
                onClick={() => navigate(`/assessment/${infectionControlAssessment.id}`)}
                className="flex items-center gap-2 px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors"
              >
                <RefreshCw size={20} />
                Retake Assessment
              </button>
            )}

            {passed && (
              <button
                onClick={handlePrint}
                className="flex items-center gap-2 px-6 py-3 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 transition-colors"
              >
                <Download size={20} />
                Download Certificate
              </button>
            )}
          </div>

          {passed && (
            <div className="border-4 border-double border-gray-800 p-8 max-w-3xl mx-auto mt-8 relative print:block print:w-full print:mt-0">
               {/* Certificate Content */}
              <div className="text-center space-y-6">
                <div className="text-4xl font-serif font-bold text-gray-800 mb-4">
                  NICE Academy Certificate
                </div>
                <div className="text-lg text-gray-600">
                  This certifies that
                </div>
                <div className="text-3xl font-cursive text-blue-800 border-b-2 border-gray-300 inline-block px-12 pb-2 mb-4">
                  {candidateDetails?.name || 'Healthcare Professional'}
                </div>
                <div className="text-lg text-gray-600">
                  has successfully completed the competency assessment for
                </div>
                <div className="text-2xl font-bold text-gray-800">
                  {infectionControlAssessment.role}
                </div>
                <div className="text-gray-600 mt-4">
                  with a score of {Math.round(score)}%
                </div>
                <div className="text-sm text-gray-500 mt-8">
                  Date: {new Date(completedAt).toLocaleDateString()}
                </div>
                
                <div className="flex justify-between items-end mt-12 px-12">
                  <div className="text-center">
                    <div className="border-t border-gray-400 w-48 mx-auto"></div>
                    <div className="text-sm text-gray-500 mt-2">NICE Academy Director</div>
                  </div>
                  <div className="w-24 h-24">
                     {/* Seal placeholder */}
                     <div className="w-full h-full rounded-full border-4 border-yellow-500 flex items-center justify-center text-yellow-600 font-bold transform rotate-[-15deg] opacity-80">
                        OFFICIAL<br/>SEAL
                     </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};
