import tkinter as tk
from tkinter import filedialog, messagebox
import re
import shutil
import datetime
from pathlib import Path

class SaveEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Simulator Save Editor (Universal)")
        self.root.geometry("620x580")
        self.root.minsize(560, 520)
        self.root.configure(bg="#151923")
        
        self.path = None
        self.data = None
        self.is_xbox = False
        
        # Colors
        self.bg = "#151923"
        self.panel = "#202736"
        self.fg = "#edf2f7"
        self.muted = "#a8b3c7"
        self.accent = "#8b7cff"
        self.green = "#5bd6a2"
        self.blue = "#3daee9"
        
        self.current_money = "—"
        self.current_level = "—"
        self.current_points = "—"
        
        self._build()

    def _build(self):
        # Header
        outer = tk.Frame(self.root, bg=self.bg, padx=26, pady=22)
        outer.pack(fill="both", expand=True)
        
        tk.Label(outer, text="SAVE EDITOR", bg=self.bg, fg=self.accent, font=("Segoe UI", 10, "bold")).pack(anchor="w")
        tk.Label(outer, text="Supermarket Simulator", bg=self.bg, fg=self.fg, font=("Segoe UI", 23, "bold")).pack(anchor="w", pady=(2, 4))
        tk.Label(outer, text="Automatic support for Steam (.es3) and Xbox (Game Pass) versions.", bg=self.bg, fg=self.muted, font=("Segoe UI", 10)).pack(anchor="w", pady=(0, 18))
        
        # File Selection
        file_row = tk.Frame(outer, bg=self.panel, padx=14, pady=12)
        file_row.pack(fill="x")
        self.file_label = tk.Label(file_row, text="No file selected", bg=self.panel, fg=self.muted, anchor="w", font=("Segoe UI", 9), wraplength=420)
        self.file_label.pack(side="left", fill="x", expand=True)
        tk.Button(file_row, text="Open Save", command=self.open_file, bg="#343f55", fg=self.fg, activebackground="#46536d", activeforeground=self.fg, relief="flat", padx=14, pady=8, cursor="hand2").pack(side="right")
        
        # Detection Area
        self.lbl_version = tk.Label(outer, text="Detected Version: None", bg=self.bg, fg=self.muted, font=("Segoe UI", 10, "bold"), anchor="w")
        self.lbl_version.pack(fill="x", pady=(10, 0))

        # Values Area
        values = tk.Frame(outer, bg=self.bg)
        values.pack(fill="x", pady=10)
        
        self.money_var = tk.StringVar()
        self.level_var = tk.StringVar()
        self.points_var = tk.StringVar()
        
        self.lbl_curr_money = self.create_edit_row(values, "Money", self.money_var)
        self.lbl_curr_level = self.create_edit_row(values, "Store Level", self.level_var)
        self.lbl_curr_points = self.create_edit_row(values, "Store Points", self.points_var)
        
        self.status = tk.Label(outer, text="Open a save file to get started.", bg=self.bg, fg=self.muted, font=("Segoe UI", 9), anchor="w")
        self.status.pack(fill="x", pady=(0, 12))
        
        # Footer
        bottom = tk.Frame(outer, bg=self.bg)
        bottom.pack(fill="x", side="bottom")
        tk.Button(bottom, text="Save Edited File", command=self.save_file, bg=self.green, fg="#151923", activebackground="#4ac793", activeforeground="#151923", relief="flat", padx=18, pady=11, font=("Segoe UI", 10, "bold"), cursor="hand2").pack(side="right")
        tk.Label(bottom, text="A secure backup will be saved in your\nDocuments folder before modifying the original.", bg=self.bg, fg=self.muted, font=("Segoe UI", 8), justify="left").pack(side="left")

    def create_edit_row(self, parent, label_text, var):
        row = tk.Frame(parent, bg=self.panel, pady=10, padx=10)
        row.pack(fill="x", pady=4)
        
        tk.Label(row, text=label_text, bg=self.panel, fg=self.fg, font=("Segoe UI", 12, "bold"), width=12, anchor="w").pack(side="left")
        
        curr_lbl = tk.Label(row, text="Current: —", bg=self.panel, fg=self.muted, font=("Segoe UI", 10), width=18, anchor="w")
        curr_lbl.pack(side="left", padx=10)
        
        entry = tk.Entry(row, textvariable=var, bg="#111722", fg=self.fg, insertbackground=self.fg, relief="flat", font=("Segoe UI", 12), highlightthickness=1, highlightbackground="#3b4760", highlightcolor=self.accent)
        entry.pack(side="right", fill="x", expand=True, ipady=4)
        
        return curr_lbl

    def open_file(self):
        chosen = filedialog.askopenfilename(title="Select the save file", filetypes=[("Files", "*.*")])
        if not chosen: return
        
        try:
            self.path = Path(chosen)
            self.data = self.path.read_bytes()
            
            # EXPLICIT VERSION DETECTION
            is_es3 = self.path.suffix.lower() == '.es3'
            stripped_data = self.data.lstrip(b'\xef\xbb\xbf \n\r\t')
            
            if is_es3 or stripped_data.startswith(b'{'):
                self.is_xbox = False
                self.lbl_version.config(text="Detected Version: STEAM (.es3 / Plain Text)", fg=self.blue)
            else:
                self.is_xbox = True
                self.lbl_version.config(text="Detected Version: XBOX / GAME PASS (Binary)", fg=self.accent)

            # Data Extraction
            m_money = re.search(rb'"Money"\s*:\s*([0-9.-]+)', self.data)
            m_level = re.search(rb'"CurrentStoreLevel"\s*:\s*([0-9.-]+)', self.data)
            m_points = re.search(rb'"CurrentStorePoint"\s*:\s*([0-9.-]+)', self.data)
            
            if not m_money or not m_level or not m_points:
                raise ValueError("Could not find the main fields in the file. Are you sure this is the correct save?")
            
            self.current_money = m_money.group(1).decode('ascii')
            self.current_level = m_level.group(1).decode('ascii')
            self.current_points = m_points.group(1).decode('ascii')
            
            self.file_label.config(text=str(self.path))
            
            self.lbl_curr_money.config(text=f"Current: {self.current_money}")
            self.lbl_curr_level.config(text=f"Current: {self.current_level}")
            self.lbl_curr_points.config(text=f"Current: {self.current_points}")
            
            self.money_var.set(self.current_money)
            self.level_var.set(self.current_level)
            self.points_var.set(self.current_points)
            
            self.status.config(text="Save loaded! Edit the values and click Save.", fg=self.green)
        except Exception as exc:
            messagebox.showerror("Open Error", str(exc))
            
    def patch_xbox_bytes(self, file_bytes, targets):
        """Surgical injection compensating exact byte size (Microsoft Store)."""
        data = bytearray(file_bytes)
        for key, new_val in targets:
            pattern = key + b'\s*:\s*([0-9.-]+)'
            match = re.search(pattern, data)
            if not match: continue
                
            start = match.start(1)
            end = match.end(1)
            old_val = data[start:end]
            
            diff = len(new_val) - len(old_val)
            data[start:end] = new_val
            
            if diff < 0:
                data[start+len(new_val):start+len(new_val)] = b' ' * (-diff)
            elif diff > 0:
                spaces_removed = 0
                search_radius = 5000
                search_start = max(0, start - search_radius)
                search_end = min(len(data), start + len(new_val) + search_radius)
                
                while spaces_removed < diff:
                    space_idx = data.find(b'  ', search_start, search_end)
                    if space_idx == -1:
                        raise ValueError(f"Not enough structure spaces to compensate for {key.decode()}. Try a smaller number.")
                    
                    del data[space_idx]
                    spaces_removed += 1
                    search_end -= 1
                    
        return bytes(data)

    def patch_steam_bytes(self, file_bytes, targets):
        """Direct replacement without worrying about byte compensation (Steam / .es3)."""
        data = file_bytes
        for key, new_val in targets:
            pattern = key + b'\s*:\s*([0-9.-]+)'
            match = re.search(pattern, data)
            if match:
                start = match.start(1)
                end = match.end(1)
                # Replace the value directly, keeping formatting and ignoring size
                data = data[:start] + new_val + data[end:]
        return data

    def save_file(self):
        if not self.data or not self.path:
            messagebox.showwarning("Warning", "Please open a save file first.")
            return
            
        try:
            float(self.money_var.get())
            int(self.level_var.get())
            int(self.points_var.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid values! Use integers for Level/Points and a dot for decimals in Money.")
            return
            
        try:
            # 1. Create Backup in Documents folder
            docs_folder = Path.home() / "Documents" / "Supermarket Simulator Backups"
            docs_folder.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{self.path.name}_{timestamp}.backup"
            backup_path = docs_folder / backup_name
            
            shutil.copy2(self.path, backup_path)
            
            # 2. Configure texts to inject
            targets = [
                (b'"Money"', str(self.money_var.get()).encode('ascii')),
                (b'"CurrentStoreLevel"', str(self.level_var.get()).encode('ascii')),
                (b'"CurrentStorePoint"', str(self.points_var.get()).encode('ascii'))
            ]
            
            # 3. Execute editing based on platform
            if self.is_xbox:
                new_bytes = self.patch_xbox_bytes(self.data, targets)
            else:
                new_bytes = self.patch_steam_bytes(self.data, targets)
            
            # 4. Overwrite original file
            self.path.write_bytes(new_bytes)
            
            # Update Interface Memory
            self.data = new_bytes
            self.lbl_curr_money.config(text=f"Current: {self.money_var.get()}")
            self.lbl_curr_level.config(text=f"Current: {self.level_var.get()}")
            self.lbl_curr_points.config(text=f"Current: {self.points_var.get()}")
            
            platform_used = "Xbox/Game Pass (Byte compensation applied)" if self.is_xbox else "Steam (Direct write applied)"
            messagebox.showinfo("Success", f"Save successfully modified!\nPlatform used: {platform_used}\n\nYour original backup is safely stored at:\n{backup_path}")
            self.status.config(text="Successfully saved and overwritten!", fg=self.green)
            
        except Exception as exc:
            messagebox.showerror("Save Error", str(exc))

if __name__ == "__main__":
    root = tk.Tk()
    SaveEditor(root)
    root.mainloop()