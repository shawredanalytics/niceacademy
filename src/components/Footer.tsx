import React from 'react';
import { Phone, Mail, Globe } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer id="contact" className="bg-gray-900 text-white pt-12 pb-8">
      <div className="container mx-auto px-4">
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">
          <div>
            <h3 className="text-xl font-bold mb-4">NICE ACADEMY</h3>
            <p className="text-gray-400 mb-4">
              NICE Academy.
              Providing assessment, training, and certification for healthcare professionals.
            </p>
          </div>
          
          <div>
            <h3 className="text-lg font-bold mb-4">Contact Us</h3>
            <div className="space-y-3">
              <div className="flex items-start gap-3">
                <div className="mt-1"><Phone size={18} className="text-blue-400" /></div>
                <div>
                  <p className="font-medium">Mr. Arepalli Srinivas (CEO)</p>
                  <p className="text-gray-400">+91 90005 57717</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Mail size={18} className="text-blue-400" />
                <a href="mailto:niceacademy.skilldevelopment@gmail.com" className="text-gray-400 hover:text-white">
                  niceacademy.skilldevelopment@gmail.com
                </a>
              </div>
            </div>
          </div>

          <div>
            <h3 className="text-lg font-bold mb-4">Certification Team</h3>
            <div className="space-y-3">
              <p className="text-gray-400">QuXAT Healthcare Systems</p>
              <div className="flex items-center gap-3">
                <Mail size={18} className="text-blue-400" />
                <a href="mailto:quxat.team@gmail.com" className="text-gray-400 hover:text-white">
                  quxat.team@gmail.com
                </a>
              </div>
              <div className="flex items-center gap-3">
                <Globe size={18} className="text-blue-400" />
                <a href="http://www.quxat.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white">
                  www.quxat.com
                </a>
              </div>
            </div>
          </div>

          <div>
            <h3 className="text-lg font-bold mb-4">Services</h3>
            <ul className="space-y-2 text-gray-400">
              <li>NABH Entry Level Certification</li>
              <li>NABL Certification</li>
              <li>Hospital Infection Control</li>
              <li>Patient Safety</li>
              <li>Facility Management</li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-800 pt-8 text-center text-gray-500">
          <p>&copy; {new Date().getFullYear()} NICE Academy. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};
