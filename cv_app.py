import streamlit as st

st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: black;
        }
        .subtitle {
            font-size: 24px;
            color: #1f77b4;
        }
        .section-title {
            font-size: 18px;
            font-weight: bold;
            color: black;
            border-bottom: 2px solid black;
            margin-bottom: 5px;
        }
        .info, .contact {
            font-size: 16px;
            line-height: 1.6;
        }
        .skills-section {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            font-size: 14px;
            margin-top: 10px;
        }
        .skills-section span {
            background: #f0f0f0;
            padding: 5px 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigate")
section = st.sidebar.radio("Go to", ["Home", "Education", "Skills", "Experience", "Certifications", "Find Me Online"])

if section == "Home":
    st.markdown('<div class="title">THEMBANI MASWANGANYI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Data Analyst</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact">📞 078 430 7885 | 📧 t.maswanganyi101@gmail.com | 🌍 South Africa, Johannesburg</div>', unsafe_allow_html=True)
    st.markdown("Welcome to my interactive CV! Use the sidebar to navigate through my experience, skills, and more.")

elif section == "Education":
    st.markdown('<div class="section-title">EDUCATION</div>', unsafe_allow_html=True)
    st.markdown("**B.Sc. Mathematical Science**  \nUniversity of Limpopo  \n01/2015 - 12/2018", unsafe_allow_html=True)
    st.markdown("**Data Science**  \nExplore AI Academy  \n01/2022 - 09/2022", unsafe_allow_html=True)

elif section == "Skills":
    st.markdown('<div class="section-title">SKILLS</div>', unsafe_allow_html=True)
   
    st.markdown("**FrontEnd**")
    st.markdown('<div class="skills-section"><span>HTML</span><span>CSS</span><span>Angular</span><span>JavaScript</span><span>Bootstrap</span></div>', unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("**Backend**")
    st.markdown('<div class="skills-section"><span>Java</span><span>Spring Framework</span><span>Hibernate</span></div>', unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("**Data Science**")
    st.markdown('<div class="skills-section"><span>NumPy</span><span>Pandas</span><span>SciPy</span><span>Scikit-Learn</span><span>Matplotlib</span><span>Seaborn</span><span>NLP</span><span>Machine Learning</span></div>', unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("**Database**")
    st.markdown('<div class="skills-section"><span>MySQL</span><span>Microsoft SQL Server</span><span>H₂ Database</span></div>', unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("**Additional**")
    st.markdown('<div class="skills-section"><span>C++</span><span>Microsoft Azure</span><span>Power BI</span><span>AWS</span></div>', unsafe_allow_html=True)

elif section == "Experience":
    st.markdown('<div class="section-title">EXPERIENCE</div>', unsafe_allow_html=True)
    
    st.markdown("**Data Analyst**  \nHarambee  \n05/2023 - Present | Johannesburg", unsafe_allow_html=True)
    st.markdown("""
    - Interpretation of technical specifications, design following principles and patterns, coding according to standards.
    - Do code-reviews and design technical documentation.
    - Assist support team and application analysts with advanced troubleshooting and support if required.
    """, unsafe_allow_html=True)

    st.markdown("**Data Analyst**  \nFNB  \n01/2022 - 12/2022 | Johannesburg", unsafe_allow_html=True)
    st.markdown("""
    - Collected, cleaned, and analyzed data from various sources to support consulting projects.
    - Assisted in the development of data models and statistical analysis to identify trends and insights.
    - Created data visualizations and dashboards using Power BI.
    """, unsafe_allow_html=True)

elif section == "Certifications":
    st.markdown('<div class="section-title">CERTIFICATION</div>', unsafe_allow_html=True)
    st.markdown("**Maths Olympiad** - AMESA", unsafe_allow_html=True)
    st.markdown("**Problem Solving (Basic)** - HackerRank", unsafe_allow_html=True)
    st.markdown("**Python** - HackerRank", unsafe_allow_html=True)

elif section == "Find Me Online":
    st.markdown('<div class="section-title">FIND ME ONLINE</div>', unsafe_allow_html=True)
    st.markdown('[Zindi Africa](https://zindi.africa/users/Thembani_Maswanganyi)', unsafe_allow_html=True)
    st.markdown('[YouTube](https://www.youtube.com/@tief_everything)', unsafe_allow_html=True)
    st.markdown('[GitHub](https://github.com/thembani47)', unsafe_allow_html=True)
    st.markdown("Thank you for viewing my interactive CV! Connect with me on any of the platforms above.")
