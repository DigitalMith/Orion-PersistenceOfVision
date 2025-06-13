@echo off
:: =================================================================
:: Orion Desktop Launcher v7 (Final Adaptation)
:: Purpose: Adapts to the limitations of this WebUI version by
::          loading the character from the default directory.
:: =================================================================

title Orion Launcher - A Persistence of Vision

:: 1. Set the correct home directory
echo [INFO] Setting Orion's home directory...
cd /d "C:\Orion\text-generation-webui"
echo [INFO] Current directory set to: %cd%
echo.

:: 2. Activate the Python virtual environment
echo [INFO] Activating Python virtual environment from 'installer_files'...
call .\installer_files\env\Scripts\activate.bat
echo.

:: 3. Execute one_click.py with supported arguments
echo [INFO] Executing one_click.py with direct arguments for Orion...
python one_click.py --model "C:\Orion\text-generation-webui\user_data\models\openhermes-2.5-mistral-7b.Q4_K_M.gguf" --loader llama.cpp --cpu --character Orion --extensions long_term_memory

:: 4. Pause on Exit for debugging
echo.
echo [INFO] Orion process has been terminated.
pause