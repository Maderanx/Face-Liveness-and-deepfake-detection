# Face-Liveness-and-Deepfake-detector
DL based Face Liveness detector

# Proposed Solution​

Saycool integrates both passive and active face liveness detection models to ensure robust and secure authentication.​

# Working​

# Passive Model:​

Initially, the system evaluates facial features such as texture, skin reflection, micro-expressions, etc. to detect liveness without user interaction.​
3D CNN Model  - Used to create the passive detection model, since a 3D CNN can capture temporal and spatial features from clips and also help in deepfake detection compared to 2D CNN models.

# Active Model:​

If the passive model does not achieve the required confidence level, the system prompts the user to perform random facial expressions (e.g., Tilting head, blinking at different speeds) to verify liveness and help eliminate deepfakes.​

LSTM Model – Used to create the active detection model, since LSTM can remember previous frames to check if someone is performing an action in real-time.​

The system provides instructions for the required actions in multiple languages to ensure accessibility and ease of use for users from different linguistic backgrounds.​

# Uses:
Remote Examinations: By preventing impersonation, liveness detection ensures exam integrity, which in turn builds trust in remote education systems and certifications, making online examinations more credible and accessible.​

Virtual Classrooms: Using liveness detection in virtual classrooms ensures students are present and attentive, thereby improving the integrity of online education and enhancing learning outcomes, leading to better overall education quality.​

E-Voting Systems: Liveness detection reduces the chances of fraudulent voting, thus strengthening the credibility of elections and increasing public trust in digital voting, leading to greater democratic participation.​

Online Transactions: By securing digital transactions, liveness detection decreases fraud, encouraging more people to engage in online banking and e-commerce, ultimately boosting confidence in the digital economy.​

Social Media Authenticity: Liveness detection helps verify real users and reduce bot-driven misinformation, enhancing the quality of online discourse and promoting a more trustworthy and reliable digital information environment.​

​


