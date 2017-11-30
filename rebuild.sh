#!/bin/sh

usage="./rebuild.sh [rpm|build]"

if [ $# -eq 0 ]; then
  echo "$usage"
  exit 0
fi

## create .rpmmacros
echo "%_topdir        $PWD" > rpmmacros_high-availability-dcache
ln -sf $PWD/rpmmacros_high-availability-dcache ~/.rpmmacros

rpms=`ls *.rpm`
specs="high-availability-dcache.spec"

case "$1" in
  rpm)
   for r in $rpms
   do
     rpm --nomd5 -ivh $r
   done
   ;;
  build)
   for s in $specs
   do
     rpmbuild --define 'dist .el6' --clean -ba SPECS/$s
   done
   ;;
esac
