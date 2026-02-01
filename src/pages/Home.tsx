import React from 'react';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';
import { AssessmentCard } from '../components/AssessmentCard';
import { infectionControlAssessment } from '../data/questions';
import { Shield, Activity, Users, FileText, Building, HeartPulse } from 'lucide-react';

export const Home: React.FC = () => {
  const services = [
    { title: 'NABH Entry Level Certification', icon: <Shield className="w-8 h-8 text-blue-600" /> },
    { title: 'NABL Certification', icon: <FileText className="w-8 h-8 text-blue-600" /> },
    { title: 'Hospital Infection Control', icon: <Activity className="w-8 h-8 text-blue-600" /> },
    { title: 'Patient Safety & Quality', icon: <HeartPulse className="w-8 h-8 text-blue-600" /> },
    { title: 'Facility Management & Safety', icon: <Building className="w-8 h-8 text-blue-600" /> },
    { title: 'Human Resource Management', icon: <Users className="w-8 h-8 text-blue-600" /> },
  ];

  const clients = [
    "Apollo Hospitals – Kakinada",
    "GVP Medical College Hospital – Visakhapatnam",
    "Aparna Hospitals – Nalgonda",
    "Dr. Sreelatha Hospitals – Nalgonda",
    "Vision Hospitals – Kakinada",
    "Shanvika Hospitals – Hyderabad",
    "Refracto Eye Hospitals – Hyderabad",
    "Shraddha Global Hospitals – Hyderabad",
    "AIMS Hospitals - Ongole",
    "Galla Hospitals – Tirupati",
    "Visakha Diabetic & Endocrine Hospitals"
  ];

  const labs = [
    "Dolphin Diagnostic Services",
    "Quality Care Speciality Lab",
    "NIMRA Medical College Hospital",
    "Sigma Diagnostics",
    "Satya Scans & Diagnostics",
    "Sai Vijaya Diagnostic Laboratory",
    "Apple Diagnostics",
    "Swathi Imaging & Diagnostics",
    "RK Scans & Diagnostics",
    "Gospel Diagnostics",
    "Aswini Diagnostics",
    "Royal Diagnostics"
  ];

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <Header />
      
      {/* Hero Section */}
      <section className="relative bg-blue-900 text-white py-20 overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <img src="/assets/hero-bg.jpg" alt="Background" className="w-full h-full object-cover" />
        </div>
        <div className="container mx-auto px-4 text-center relative z-10">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">
            NICE Academy
          </h1>
          <p className="text-xl md:text-2xl text-blue-100 max-w-3xl mx-auto mb-10">
            Empowering Healthcare Professionals through Competency Assessment, Training, and Certification.
          </p>
          <a 
            href="#assessments" 
            className="inline-block bg-white text-blue-800 font-bold py-3 px-8 rounded-full hover:bg-blue-50 transition-colors shadow-lg"
          >
            Start Assessment
          </a>
        </div>
      </section>

      <main className="flex-grow">
        {/* About Section */}
        <section className="py-16 container mx-auto px-4">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">About NICE Academy</h2>
              <p className="text-lg text-gray-700 mb-4">
                NICE Academy is dedicated to improving healthcare standards through rigorous training and assessment. 
                We provide comprehensive certification programs for hospitals and healthcare professionals.
              </p>
              <p className="text-lg text-gray-700">
                Our programs cover a wide range of critical areas including Infection Control, Patient Safety, 
                Quality Improvement, and Facility Management.
              </p>
            </div>
            <div className="relative h-full min-h-[400px]">
               <img 
                 src="/assets/about-section.jpg" 
                 alt="About NICE Academy" 
                 className="absolute inset-0 w-full h-full object-cover rounded-2xl shadow-xl" 
               />
               <div className="absolute inset-0 bg-blue-900/10 rounded-2xl"></div>
            </div>
          </div>
        </section>

        {/* Available Assessments */}
        <section id="assessments" className="py-16 bg-gray-100">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
              Available Competency Assessments
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 justify-center">
              <AssessmentCard assessment={infectionControlAssessment} />
              {/* More assessments can be added here */}
            </div>
          </div>
        </section>

        {/* Services Section */}
        <section id="services" className="py-16 container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
            Our Key Services
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <div key={index} className="bg-white p-6 rounded-xl shadow-md border border-gray-100 flex items-start gap-4 hover:shadow-lg transition-shadow">
                <div className="bg-blue-50 p-3 rounded-lg">
                  {service.icon}
                </div>
                <div>
                  <h3 className="text-xl font-semibold text-gray-800 mb-2">{service.title}</h3>
                  <p className="text-gray-600 text-sm">
                    Comprehensive training and certification protocols.
                  </p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Clients Section */}
        <section className="py-16 bg-white border-t border-gray-100">
          <div className="container mx-auto px-4">
            <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
              Our Trusted Clients
            </h2>
            
            <div className="mb-10">
              <h3 className="text-xl font-semibold text-center text-blue-800 mb-6">Hospitals</h3>
              <div className="flex flex-wrap justify-center gap-4">
                {clients.map((client, index) => (
                  <span key={index} className="px-4 py-2 bg-gray-100 rounded-full text-gray-700 font-medium text-sm">
                    {client}
                  </span>
                ))}
              </div>
            </div>

            <div>
              <h3 className="text-xl font-semibold text-center text-blue-800 mb-6">Diagnostic Laboratories</h3>
              <div className="flex flex-wrap justify-center gap-4">
                {labs.map((lab, index) => (
                  <span key={index} className="px-4 py-2 bg-gray-100 rounded-full text-gray-700 font-medium text-sm">
                    {lab}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
};
