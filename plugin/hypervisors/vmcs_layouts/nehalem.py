
 #
 # VMCS Memory layout converted from Google Rekall Repository with
 # rekall2actaeon.py 
 #
 # Authors: 
 # Mariano `emdel` Graziano - graziano@eurecom.fr
 #
 # This program is free software; you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation; either version 2 of the License, or (at
 # your option) any later version.
 #
 # This program is distributed in the hope that it will be useful, but
 # WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 # General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program; if not, write to the Free Software
 # Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 #



vmcs = {
"GUEST_FS_ATTR": 0x9d,
"HOST_IA32_PAT_HIGH": 0xc9,
"VIRTUAL_APIC_PAGE_ADDR_HIGH": 0x39,
"APIC_ACCESS_ADDR": 0x1e,
"GUEST_FS_BASE": 0x9a,
"GUEST_IA32_EFER_HIGH": 0x45,
"GUEST_IDTR_BASE": 0xb2,
"CR0_READ_SHADOW": 0xf4,
"ENTRY_EXCEPTION_ERROR_CODE": 0x55,
"HOST_SS_SEL": 0xc2,
"GUEST_VMX_PREEMTION_TIMER": 0x58,
"HOST_IA32_SYSENTER_CS": 0xe6,
"GUEST_SS_ATTR": 0x91,
"GUEST_ACTIVITY_STATE": 0x63,
"HOST_DS_SEL": 0xc3,
"EXIT_MSR_LOAD_COUNT": 0x51,
"ENTRY_MSR_LOAD_ADDR_HIGH": 0x33,
"PAGEFAULT_ERRCODE_MASK": 0x4c,
"IO_BITMAP_A": 0x28,
"IDT_VECTORING_ERRCODE": 0x5f,
"ABORT_INDICATOR": 0x1,
"GUEST_IDTR_LIMIT": 0xb5,
"CR4_READ_SHADOW": 0xf6,
"GUEST_IA32_SYSENTER_CS": 0x65,
"GUEST_IA32_PAT_HIGH": 0x43,
"IS_SHADOW_VMCS": 0x0,
"EPT_POINTER": 0x3a,
"GUEST_PENDING_DEBUG_EXCEPT": 0x7a,
"GUEST_ES_BASE": 0x82,
"HOST_FS_BASE": 0xd4,
"HOST_FS_SEL": 0xc4,
"GUEST_PDPTE2": 0xec,
"GUEST_PHYSICAL_ADDR": 0x3c,
"VPID": 0xbc,
"HOST_CR3": 0xd0,
"HOST_CR0": 0xce,
"HOST_CR4": 0xd2,
"GUEST_TR_ATTR": 0xaf,
"GUEST_PDPTE2_HIGH": 0xed,
"REVISION_ID": 0x0,
"GUEST_CS_BASE": 0x88,
"GUEST_RFLAGS": 0x78,
"GUEST_SS_LIMIT": 0x90,
"HOST_IA32_EFER_HIGH": 0xcb,
"IO_RCX": 0x68,
"IO_BITMAP_B_HIGH": 0x2b,
"GUEST_SS_BASE": 0x8e,
"GUEST_IA32_SYSENTER_ESP": 0x7c,
"ENTRY_MSR_LOAD_ADDR": 0x32,
"EXIT_INSTR_LEN": 0x60,
"GUEST_IA32_DEBUGCTL": 0x40,
"GUEST_LDTR_ATTR": 0xa9,
"HOST_ES_SEL": 0xc0,
"EXIT_INTERRUPT_INFO": 0x5c,
"GUEST_LDTR_LIMIT": 0xa8,
"GUEST_DS_LIMIT": 0x96,
"GUEST_RIP": 0x76,
"GUEST_IA32_PERF_CTL": 0x46,
"GUEST_TR_LIMIT": 0xae,
"PAGEFAULT_ERRCODE_MATCH": 0x4d,
"INSTR_INFO": 0x61,
"GUEST_GDTR_LIMIT": 0xb4,
"GUEST_DS_BASE": 0x94,
"CR3_TARGET_3": 0xfe,
"HOST_TR_SEL": 0xc6,
"CR3_TARGET_1": 0xfa,
"CR3_TARGET_0": 0xf8,
"HOST_GS_BASE": 0xd6,
"GUEST_FS_LIMIT": 0x9c,
"IO_RDI": 0x6c,
"MSR_BITMAP_HIGH": 0x2d,
"GUEST_FS_SEL": 0x98,
"EXIT_CONTROLS": 0x4f,
"IO_RSI": 0x6a,
"ENTRY_INSTR_LENGTH": 0x56,
"GUEST_ES_LIMIT": 0x84,
"GUEST_GS_BASE": 0xa0,
"GUEST_CS_ATTR": 0x8b,
"HOST_CS_SEL": 0xc1,
"IDT_VECTORING_INFO_FIELD": 0x5e,
"ENTRY_INT_INFO_FIELD": 0x54,
"GUEST_INTERRUPT_STATUS": 0xaa,
"GUEST_LDTR_BASE": 0xa6,
"GUEST_PDPTE3_HIGH": 0xef,
"GUEST_CS_SEL": 0x86,
"TPR_THRESHOLD": 0x57,
"TSC_OFFSET_HIGH": 0x37,
"GUEST_DS_SEL": 0x92,
"GUEST_LINEAR_ADDR": 0x70,
"HOST_IA32_SYSENTER_EIP": 0xe0,
"GUEST_ES_ATTR": 0x85,
"EXIT_REASON": 0x5b,
"GUEST_PHYSICAL_ADDR_HIGH": 0x3d,
"HOST_IA32_EFER": 0xca,
"GUEST_GS_LIMIT": 0xa2,
"GUEST_GS_SEL": 0x9e,
"APIC_ACCESS_ADDR_HIGH": 0x1f,
"GUEST_SMBASE": 0x64,
"HOST_IA32_PAT": 0xc8,
"HOST_GS_SEL": 0xc5,
"CR3_TARGET_COUNT": 0x4e,
"HOST_RSP": 0xe2,
"HOST_RIP": 0xe4,
"PROC_VM_EXEC_CONTROLS2": 0x49,
"EXIT_MSR_STORE_ADDR": 0x2e,
"IO_BITMAP_A_HIGH": 0x29,
"EXECUTIVE_VMCS_PTR": 0x34,
"HOST_IA32_PERF_CTL": 0xcc,
"HOST_TR_BASE": 0xd8,
"GUEST_CS_LIMIT": 0x8a,
"EXIT_QUALIFICATION": 0x66,
"EXIT_INTERRUPT_ERRCODE": 0x5d,
"EXCEPTION_BITMAP": 0x4b,
"PROC_VM_EXEC_CONTROLS": 0x48,
"GUEST_PDPTE1_HIGH": 0xeb,
"GUEST_LDTR_SEL": 0xa4,
"HOST_GDTR_BASE": 0xda,
"IO_RIP": 0x6e,
"ENTRY_CONTROLS": 0x52,
"GUEST_PDPTE0_HIGH": 0xe9,
"GUEST_IA32_PAT": 0x42,
"CR3_TARGET_2": 0xfc,
"GUEST_GS_ATTR": 0xa3,
"GUEST_TR_SEL": 0xaa,
"HOST_IA32_SYSENTER_ESP": 0xde,
"GUEST_IA32_DEBUGCTL_HIGH": 0x41,
"IO_BITMAP_B": 0x2a,
"GUEST_PDPTE0": 0xe8,
"EPT_POINTER_HIGH": 0x3b,
"GUEST_GDTR_BASE": 0xb0,
"INSTR_ERROR": 0x3,
"VIRTUAL_APIC_PAGE_ADDR": 0x38,
"GUEST_PDPTE3": 0xee,
"GUEST_CR0": 0xb6,
"GUEST_CR3": 0xb8,
"GUEST_CR4": 0xba,
"HOST_IDTR_BASE": 0xdc,
"GUEST_PDPTE1": 0xea,
"EXIT_MSR_LOAD_ADDR": 0x30,
"CR4_MASK": 0xf2,
"ENTRY_MSR_LOAD_COUNT": 0x53,
"GUEST_IA32_EFER": 0x44,
"PIN_VM_EXEC_CONTROLS": 0x4a,
"GUEST_SS_SEL": 0x8c,
"HOST_IA32_PERF_CTL_HIGH": 0xcd,
"GUEST_DR7": 0x72,
"GUEST_DS_ATTR": 0x97,
"CR0_MASK": 0xf0,
"EXECUTIVE_VMCS_PTR_HIGH": 0x35,
"VMCS_LINK_POINTER": 0x3e,
"GUEST_ES_SEL": 0x80,
"VMCS_LINK_PTR_HIGH": 0x3f,
"MSR_BITMAP": 0x2c,
"GUEST_IA32_PERF_CTL_HIGH": 0x47,
"EXIT_MSR_STORE_ADDR_HIGH": 0x2f,
"EXIT_MSR_LOAD_ADDR_HIGH": 0x31,
"GUEST_RSP": 0x74,
"TSC_OFFSET": 0x36,
"GUEST_IA32_SYSENTER_EIP": 0x7e,
"GUEST_INTERRUPTIBILITY_INFO": 0x62,
"EXIT_MSR_STORE_COUNT": 0x50,
"GUEST_TR_BASE": 0xac
}