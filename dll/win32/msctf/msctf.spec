@ stdcall -private DllCanUnloadNow()
@ stdcall -private DllGetClassObject(ptr ptr ptr)
@ stdcall -private DllRegisterServer()
@ stdcall -private DllUnregisterServer()
@ stdcall SetInputScope(long long)
@ stub SetInputScopeXML
@ stdcall SetInputScopes(long ptr long ptr long wstr wstr)
@ stub TF_CUASAppFix
@ stdcall -stub TF_CheckThreadInputIdle(long long)
@ stub TF_ClearLangBarAddIns
@ stdcall -stub TF_CreateCategoryMgr(ptr)
@ stdcall -stub TF_CreateCicLoadMutex(ptr)
@ stdcall -stub TF_CreateDisplayAttributeMgr(ptr)
@ stdcall TF_CreateInputProcessorProfiles(ptr)
@ stdcall TF_CreateLangBarItemMgr(ptr)
@ stdcall TF_CreateLangBarMgr(ptr)
@ stdcall TF_CreateThreadMgr(ptr)
@ stdcall -stub TF_DllDetachInOther()
@ stdcall -stub TF_GetGlobalCompartment(ptr)
@ stub TF_GetInputScope
@ stdcall -stub TF_GetLangIcon(long ptr long)
@ stdcall -stub TF_GetMlngHKL(long ptr ptr long)
@ stdcall -stub TF_GetMlngIconIndex(long)
@ stdcall -stub TF_GetThreadFlags(long ptr ptr ptr)
@ stdcall TF_GetThreadMgr(ptr)
@ stdcall -stub TF_InatExtractIcon(long)
@ stdcall TF_InitMlngInfo()
@ stdcall -stub TF_InitSystem()
@ stdcall -stub TF_UninitSystem()
@ stdcall -stub TF_InvalidAssemblyListCache()
@ stdcall TF_InvalidAssemblyListCacheIfExist()
@ stdcall TF_IsCtfmonRunning()
@ stdcall -stub TF_IsInMarshaling(long)
@ stdcall -stub TF_MlngInfoCount()
@ stdcall TF_RunInputCPL()
@ stdcall -stub TF_PostAllThreadMsg(long long)
@ stdcall TF_RegisterLangBarAddIn(ptr wstr long)
@ stdcall TF_UnregisterLangBarAddIn(ptr long)
