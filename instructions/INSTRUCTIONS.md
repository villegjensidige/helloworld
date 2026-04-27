# Step-by-Step Analysis Logic

1. **Extract Data**: Identify the Patient Name, Date, and requested Procedure/Item from the document.
2. **Verify**: Check if the Procedure/Item exists in `REGISTER.md`. 
3. **Check Exceptions**: Check if the Procedure/Item exists in `EXCEPTIONS.md`.
4. **Determine Status**: 
   - If it is in the Register AND NOT in Exceptions -> Status is "Approved".
   - If it is in Exceptions -> Status is "Denied".
   - If it is in neither -> Status is "Manual Review Required".