# PIL may use low-level file-descriptor writes; encode in memory, then write atomically.
import io,os
from pathlib import Path
from PIL import Image
original_save=Image.Image.save
def safe_save(self,fp,format=None,**params):
 if not isinstance(fp,(str,Path)):
  return original_save(self,fp,format=format,**params)
 path=Path(fp);fmt=format or Image.registered_extensions()[path.suffix.lower()];buf=io.BytesIO();original_save(self,buf,format=fmt,**params);data=buf.getvalue();temp=path.with_name(path.name+'.tmp')
 with temp.open('wb') as f:
  n=f.write(data);f.flush();os.fsync(f.fileno())
 if n!=len(data) or temp.stat().st_size!=len(data):raise OSError('Incomplete image write')
 temp.replace(path)
Image.Image.save=safe_save
