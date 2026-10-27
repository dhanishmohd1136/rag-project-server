import os
from dotenv import load_dotenv
from supabase import create_client,Client


supabase_url = os.getenv("SUPABASE_API_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError ("Missing supabase credential in enveronment variable")


supabase : Client = create_client(supabase_url,supabase_key)