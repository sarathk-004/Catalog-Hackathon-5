# Electronic Voting System

## Overview
The Electronic Voting System is a console-based application designed to facilitate secure and tamper-proof voting. This system ensures that votes are cast anonymously and cannot be altered after submission. The system includes features such as OTP validation to prevent unauthorized access and vote tampering.

## Features
- **OTP Verification**: Each voter receives a unique OTP (One-Time Password) to validate their identity before casting a vote.
- **Vote Confirmation**: Voters must confirm their choice before their vote is recorded.
- **Tamper-Proof Voting**: Votes are hashed to prevent tampering and ensure integrity.
- **Results Display**: Voting results are displayed in a clean, tabular format after validating all votes.

## Code Explanation
- **generate_otp(voter_id)**: Generates a unique OTP for each voter and stores it in a file.
- **validate_otp(voter_id, entered_otp)**: Validates the entered OTP against the stored OTP.
- **hash_vote(voter_id, choice)**: Hashes the vote data to ensure its integrity.
- **cast_vote(voter_id)**: Allows the voter to select a candidate and confirm their vote.
- **validate_votes()**: Ensures that all votes have not been tampered with by re-validating them.
- **display_results()**: Displays the voting results in a tabular format using the tabulate library.
