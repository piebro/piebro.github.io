# How to import music to an old iPod Nano using a VM

I've recently rediscovered my old iPod Nano and wanted to add some music to it.
I spent some time testing various software options available for Ubuntu, including libgpod, gtkpod, and even some Python scripts, but none of them worked for my iPod Nano 3rd generation.

After much trial and error, I found a solution that should stand the test of time: running iTunes through a Windows XP virtual machine.
I hope that this is a robust approach that will continue working for years to come.

## Setting Up the Virtual Machine Environment

First, we need to set up KVM (Kernel-based Virtual Machine) on Ubuntu. Start by installing KVM and its required components and adding your user to the necessary groups to manage virtual machines.
```bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
sudo adduser $USER libvirt
sudo adduser $USER kvm
```

Enable and start the libvirt service and verify that everything is working correctly.
```bash
sudo systemctl enable --now libvirtd
sudo systemctl start libvirtd
virsh list --all
```

Launch Virtual Machine Manager using the command: `virt-manager`.

## Setting Up Windows XP

I am using Windows XP because it's easy to install and that's what I used when I first got my iPod.

Download the [Windows XP Professional SP3 ISO](https://archive.org/details/en_windows_xp_professional_with_service_pack_3_x86_cd_vl_x14-73974_202202) and [iTunes for WinXP](https://archive.org/details/i-tunes-setup-12.1.3.6-windows-xp-32-bit) from the Internet Archive.
Then install the ISO and activate it using the activation keys from this GitHub repository: [Windows XP Keys](https://github.com/Fuwn/xp)

## Connecting Your iPod

In my testing, regular USB drives and internet connectivity were problematic in the VM. However, I could use the iPod itself as a storage device to transfer the necessary files.
Before starting the VM, I connect the iPod to my computer via USB and use it as a storage device to save the iTunes.exe and my music files.

Then I start the VM and connect and pass the iPod to the VM via USB passthrough. (On KVM it's done by clicking `Add New Hardware` => `USB Host Device` => `select the iPod from the list`)

After doing this, the iPod should now appear as a drive in Windows XP.
Copy the iTunes installer and the music files to Windows XP and install iTunes.

Once iTunes is installed and running, you should be able to use it normally to manage your iPod. The software will recognize your device and allow you to sync music.
